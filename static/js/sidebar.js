document.addEventListener('DOMContentLoaded', function () {
    const sidebar = document.getElementById('sidebar')
    const toggleBtn = document.getElementById('toggleBtn')
    const toggleIcon = document.getElementById('toggleIcon')
    const mainContent = document.getElementById('mainContent')
  
    toggleBtn.addEventListener('click', function () {
      sidebar.classList.toggle('sidebar-collapsed')
      toggleIcon.classList.toggle('icon-rotate')
  
      if (sidebar.classList.contains('sidebar-collapsed')) {
        toggleBtn.style.transform = 'translateX(-0.1rem)'
      } else {
        toggleBtn.style.transform = 'translateX(0)'
      }
    })
  })