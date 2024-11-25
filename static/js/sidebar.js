document.addEventListener('DOMContentLoaded', function () {
  const sidebar = document.getElementById('sidebar');
  const toggleBtn = document.getElementById('toggleBtn');
  const toggleIcon = document.getElementById('toggleIcon');
  const mainContent = document.getElementById('mainContent');
  
  let tableInstance = null; 

  function initializeDataTable() {
      if (tableInstance) {
          tableInstance.destroy(); 
      }

      tableInstance = $('#tablePerhitungan').DataTable({
          paging: true,
          searching: true,
          ordering: true,
          info: true,
          autoWidth: false,
          scrollX: true,
      });
  }

  function reinitializeDataTable() {
      if (tableInstance) {
          tableInstance.destroy(); 
      }

      tableInstance = $('#tablePerhitungan').DataTable({
          paging: true,
          searching: true,
          ordering: true,
          info: true,
          autoWidth: false,
          scrollX: false,
      });
  }

  toggleBtn.addEventListener('click', function () {
      sidebar.classList.toggle('sidebar-collapsed');
      toggleIcon.classList.toggle('icon-rotate');

      if (sidebar.classList.contains('sidebar-collapsed')) {
          toggleBtn.style.transform = 'translateX(-0.1rem)';
          mainContent.classList.remove('w-4/5');
          mainContent.classList.add('w-full');

          reinitializeDataTable();
      } else {
          toggleBtn.style.transform = 'translateX(0)';
          mainContent.classList.remove('w-full');
          mainContent.classList.add('w-4/5');

          initializeDataTable();
      }
  });

  initializeDataTable();
});
