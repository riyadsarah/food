
console.log('Hello World');

window.addEventListener("load", function(){
    const preloader = document.querySelector(".preloader");
    preloader.classList.add("preloader-finish");
  });




  
  

      function tampilkanJam() {
        var waktu = new Date();
        var jam = waktu.getHours();
        var menit = waktu.getMinutes();
        var detik = waktu.getSeconds();

        var tanggal = waktu.getDate();
        var bulan = waktu.getMonth();
        var tahun = waktu.getFullYear();

        // Tambahkan 0 didepan angka jika kurang dari 10
        if (jam < 10) {
            jam = "0" + jam;
        }
        if (menit < 10) {
            menit = "0" + menit;
        }
        if (detik < 10) {
            detik = "0" + detik;
        }

        document.getElementById("jam").innerHTML = jam + ":" + menit + ":" + detik;
        document.getElementById("tanggal").innerHTML = tanggal + "-" + (bulan + 1) + "-" + tahun;

        setTimeout("tampilkanJam()", 1000);
    }
    tampilkanJam();



    









// kalkilator

      input1.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
        submitButton.click();
        }
        });
        
        input2.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
        submitButton.click();
        }
        });





      // This example uses jQuery
$(document).ready(function() {
  $('.product-card').click(function() {
    $(this).toggleClass('flipped');
  });
});

//hgkhgkjygkj

html2canvas(document.querySelector("#barcode2")).then(canvas => {
  // Convert canvas to image
  var img = canvas.toDataURL("image/png");

  // Create a link and trigger download
  var link = document.createElement('a');
  link.download = 'barcode.png';
  link.href = img;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
});





