var x = 0;

function addInput() {
	if (x < 3) {
    var str = '<input type="text" class="link" placeholder="Ссылка на профиль *"> <input type="text" class="amount" placeholder="Кол-во"> <div id="input' + (x + 1) + '"></div>';
    document.getElementById('input' + x).innerHTML = str;
    x++;
  } else
  {
  	alert('STOP it!');
  }
}
