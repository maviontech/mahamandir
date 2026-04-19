/* Swarved Mahamandir — admin panel
 * Drag-and-drop reorder + CSRF helper.
 */
(function () {
  'use strict';

  function getCookie(name) {
    const m = document.cookie.match(new RegExp('(^|; )' + name + '=([^;]+)'));
    return m ? decodeURIComponent(m[2]) : null;
  }
  const csrftoken = getCookie('csrftoken');

  // ---------------------------------------------------------------
  // Sortable containers — HTML5 drag & drop
  // ---------------------------------------------------------------
  document.querySelectorAll('.admin-sortable').forEach(container => {
    const url = container.dataset.reorderUrl;
    if (!url) return;

    const items = container.querySelectorAll('.admin-row, .admin-image-card');
    items.forEach(item => {
      item.setAttribute('draggable', 'true');

      item.addEventListener('dragstart', (e) => {
        item.classList.add('is-dragging');
        e.dataTransfer.effectAllowed = 'move';
        e.dataTransfer.setData('text/plain', item.dataset.id);
      });
      item.addEventListener('dragend', () => {
        item.classList.remove('is-dragging');
        persist();
      });
    });

    container.addEventListener('dragover', (e) => {
      e.preventDefault();
      const dragging = container.querySelector('.is-dragging');
      if (!dragging) return;
      const after = getDragAfter(container, e.clientY);
      if (after == null) container.appendChild(dragging);
      else container.insertBefore(dragging, after);
    });

    function getDragAfter(parent, y) {
      const siblings = [...parent.querySelectorAll('.admin-row:not(.is-dragging), .admin-image-card:not(.is-dragging)')];
      return siblings.reduce((closest, child) => {
        const box = child.getBoundingClientRect();
        const offset = y - box.top - box.height / 2;
        if (offset < 0 && offset > closest.offset) return { offset, elem: child };
        return closest;
      }, { offset: Number.NEGATIVE_INFINITY }).elem;
    }

    function persist() {
      const ids = [...container.querySelectorAll('[data-id]')].map(el => Number(el.dataset.id));
      fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken },
        body: JSON.stringify(ids),
      }).then(r => {
        if (r.ok) flash('Order saved', 'ok');
        else flash('Could not save order', 'error');
      }).catch(() => flash('Network error', 'error'));
    }
  });

  // ---------------------------------------------------------------
  // Ephemeral flash (top-right toast)
  // ---------------------------------------------------------------
  function flash(text, kind) {
    const el = document.createElement('div');
    el.className = 'admin-toast admin-toast--' + (kind || 'info');
    el.textContent = text;
    document.body.appendChild(el);
    requestAnimationFrame(() => el.classList.add('is-in'));
    setTimeout(() => {
      el.classList.remove('is-in');
      setTimeout(() => el.remove(), 300);
    }, 1800);
  }

  // Inject toast CSS once
  const style = document.createElement('style');
  style.textContent = `
    .admin-toast {
      position: fixed; bottom: 1.5rem; right: 1.5rem; z-index: 9999;
      background: #2A1810; color: #FDF4D9; padding: .75rem 1.25rem;
      border-radius: 10px; box-shadow: 0 10px 30px rgba(0,0,0,.25);
      transform: translateY(20px); opacity: 0; transition: all .3s ease;
      font-size: .9rem; font-family: Inter, sans-serif;
    }
    .admin-toast.is-in { transform: translateY(0); opacity: 1; }
    .admin-toast--ok { background: #3E8040; }
    .admin-toast--error { background: #B94A2C; }
  `;
  document.head.appendChild(style);

  // ---------------------------------------------------------------
  // Image preview on file input change
  // ---------------------------------------------------------------
  document.querySelectorAll('input[type="file"]').forEach(input => {
    input.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (!file || !file.type.startsWith('image/')) return;
      let preview = input.parentElement.querySelector('.admin-inline-preview');
      if (!preview) {
        preview = document.createElement('img');
        preview.className = 'admin-inline-preview';
        preview.style.cssText = 'max-width:240px;max-height:180px;margin-top:.75rem;border-radius:6px;border:1px solid #E6D5B5;display:block;';
        input.parentElement.appendChild(preview);
      }
      preview.src = URL.createObjectURL(file);
    });
  });

})();
