function konfirmasiHapus(deleteUrl) {
    Swal.fire({
      title: 'Apakah Anda yakin?',
      text: 'Data ini akan dihapus secara permanen!',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#d33',
      cancelButtonColor: '#3085d6',
      confirmButtonText: 'Ya, hapus!',
      cancelButtonText: 'Batal'
    }).then((result) => {
      if (result.isConfirmed) {
        $.ajax({
          url: deleteUrl,
          type: 'POST',
          success: function (response) {
            if (response.success) {
              Swal.fire({
                title: 'Terhapus!',
                text: 'Data berhasil dihapus.',
                icon: 'success',
                confirmButtonText: 'OK'
              }).then(() => {
                location.reload()
              })
            } else {
              Swal.fire({
                title: 'Gagal',
                text: 'Data tidak berhasil dihapus.',
                icon: 'error',
                confirmButtonText: 'OK'
              })
            }
          },
          error: function () {
            Swal.fire({
              title: 'Terjadi Kesalahan',
              text: 'Tidak dapat menghapus data.',
              icon: 'error',
              confirmButtonText: 'OK'
            })
          }
        })
      }
    })
  }