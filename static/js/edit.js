function openModalEdit() {
    const modal = document.getElementById('modalEdit')
    const modalContent = document.getElementById('modalContentEdit')
  
    modal.classList.remove('hidden')
    modal.classList.add('flex')
  
    setTimeout(() => {
      modalContent.classList.remove('opacity-0', 'scale-95')
      modalContent.classList.add('opacity-100', 'scale-100')
    }, 10)
  }
  
  function closeModalEdit() {
    const modal = document.getElementById('modalEdit')
    const modalContent = document.getElementById('modalContentEdit')
  
    modalContent.classList.remove('opacity-100', 'scale-100')
    modalContent.classList.add('opacity-0', 'scale-95')
  
    setTimeout(() => {
      modal.classList.add('hidden')
      modal.classList.remove('flex')
    }, 300)
  }
  
  window.addEventListener('click', (event) => {
    const modal = document.getElementById('modalEdit')
    if (event.target === modal) {
      closeModal()
    }
  })
  
  document.addEventListener('DOMContentLoaded', function () {
    const editButtons = document.querySelectorAll('.edit-button')
  
    editButtons.forEach((button) => {
      button.addEventListener('click', function () {
        const kodeKriteria = button.getAttribute('data-kode')
        const kriteria = button.getAttribute('data-kriteria')
        const jenisKriteria = button.getAttribute('data-jenis')
  
        document.getElementById('kodeKriteria').value = kodeKriteria
        document.getElementById('kriteria').value = kriteria
        document.getElementById('jenisKriteria').value = jenisKriteria
      })
    })
  })
  $('#editKriteria').on('submit', function (event) {
    event.preventDefault()
  
    const kodeKriteria = $('#kodeKriteria').val()
  
    $.ajax({
      url: `/edit/${kodeKriteria}`,
      type: 'POST',
      data: $('#editKriteria').serialize(),
      success: function (response) {
        if (response.success) {
          Swal.fire({
            title: response.message,
            icon: 'success',
            confirmButtonText: 'OK'
          }).then((result) => {
            if (result.isConfirmed) {
              location.reload()
            }
          })
          closeModalEdit()
        } else {
          Swal.fire({
            title: 'Gagal Mengubah Data',
            icon: 'error',
            confirmButtonText: 'OK'
          })
        }
      },
      error: function () {
        Swal.fire({
          title: 'Terjadi Kesalahan',
          icon: 'error',
          confirmButtonText: 'OK'
        })
      }
    })
  })