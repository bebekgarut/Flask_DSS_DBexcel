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

  document.addEventListener('DOMContentLoaded', function () {
    const editButtons = document.querySelectorAll('.edit-button-user')
  
    editButtons.forEach((button) => {
      button.addEventListener('click', function () {
        const email = button.getAttribute('data-email')
        const username = button.getAttribute('data-username')
        const password = button.getAttribute('data-password')
        const id = button.getAttribute('data-id')
  
        
        document.getElementById('id').value = id
        document.getElementById('email').value = email
        document.getElementById('username').value = username
        document.getElementById('password').value = password
      })
    })
  })

  $('#editUser').on('submit', function (event) {
    event.preventDefault()
  
    const id = $('#id').val()
  
    $.ajax({
      url: `/user/edit/${id}`,
      type: 'POST',
      data: $('#editUser').serialize(),
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

  document.querySelectorAll('.edit-button-ahli').forEach(button => {
    button.addEventListener('click', function() {
      const row = this.closest('tr');
      const rowData = {};
      
      row.querySelectorAll('td').forEach((cell, index) => {
        const colName = document.querySelectorAll('th')[index].innerText; // Dapatkan nama kolom dari header
        rowData[colName] = cell.innerText;
      });
      
      // Log untuk cek `rowData` sebelum pengisian input di modal
      console.log("Data Baris Terpilih:", rowData);
      
      // Isi setiap input di modal berdasarkan rowData
      Object.entries(rowData).forEach(([key, value]) => {
        const input = document.getElementById(`input_${key}`);
        if (input) {
          input.value = value; 
        } else {
          console.log(`Input dengan ID input_${key} tidak ditemukan`);
        }
      
      });
      
    });
  });

  $('#editAhli').on('submit', function (event) {
    event.preventDefault()
  
    const kodeAhli = $('#input_kode_ahli').val()
  
    $.ajax({
      url: `/ahli/edit/${kodeAhli}`,
      type: 'POST',
      data: $('#editAhli').serialize(),
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

  document.querySelectorAll('.edit-button-alternatif').forEach(button => {
    button.addEventListener('click', function() {
      const row = this.closest('tr');
      const rowData = {};
      
      row.querySelectorAll('td').forEach((cell, index) => {
        const colName = document.querySelectorAll('th')[index].innerText; // Dapatkan nama kolom dari header
        rowData[colName] = cell.innerText;
      });
      
      console.log("Data Baris Terpilih:", rowData);
      
      Object.entries(rowData).forEach(([key, value]) => {
        const input = document.getElementById(`input_${key}`);
        if (input) {
          input.value = value; 
        } else {
          console.log(`Input dengan ID input_${key} tidak ditemukan`);
        }
      
      });
      
    });
  });
  
  