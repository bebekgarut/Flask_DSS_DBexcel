function openModal() {
    const modal = document.getElementById('modalTambah')
    const modalContent = document.getElementById('modalContentTambah')
  
    modal.classList.remove('hidden')
    modal.classList.add('flex')
  
    setTimeout(() => {
      modalContent.classList.remove('opacity-0', 'scale-95')
      modalContent.classList.add('opacity-100', 'scale-100')
    }, 10)
  }
  
function closeModal() {
    const modal = document.getElementById('modalTambah')
    const modalContent = document.getElementById('modalContentTambah')
  
    modalContent.classList.remove('opacity-100', 'scale-100')
    modalContent.classList.add('opacity-0', 'scale-95')
  
    setTimeout(() => {
      modal.classList.add('hidden')
      modal.classList.remove('flex')
    }, 300)
  }
  
window.addEventListener('click', (event) => {
    const modal = document.getElementById('modalTambah')
    if (event.target === modal) {
      closeModal()
    }
  })
  
$('#tambahKriteria').on('submit', function (event) {
    event.preventDefault()
  
    $.ajax({
      url: '/tambah',
      type: 'POST',
      data: $('#tambahKriteria').serialize(),
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
          closeModal()
        } else {
          Swal.fire({
            title: 'Gagal Menambahkan Data',
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

  $('#tambahAhli').on('submit', function (event) {
    event.preventDefault()
  
    $.ajax({
      url: 'ahli/tambah',
      type: 'POST',
      data: $('#tambahAhli').serialize(),
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
          closeModal()
        } else {
          Swal.fire({
            title: 'Gagal Menambahkan Data',
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

  $('#tambahAlternatif').on('submit', function (event) {
    event.preventDefault()
  
    $.ajax({
      url: 'alternatif/tambah',
      type: 'POST',
      data: $('#tambahAlternatif').serialize(),
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
          closeModal()
        } else {
          Swal.fire({
            title: 'Gagal Menambahkan Data',
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


  $('#tambahUser').on('submit', function (event) {
    event.preventDefault()
  
    $.ajax({
      url: 'user/tambah',
      type: 'POST',
      data: $('#tambahUser').serialize(),
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
          closeModal()
        } else {
          Swal.fire({
            title: 'Gagal Menambahkan Data',
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
