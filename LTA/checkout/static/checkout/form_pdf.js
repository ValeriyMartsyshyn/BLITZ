function download() {
  var element = document.createElement('a');
  element.setAttribute('href', "./pdf");
  element.setAttribute('target', "_blank");
  element.setAttribute('download', 'plan.html');

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

$('#form').click(function(){
    $.get('./update_pdf').done(download)
})