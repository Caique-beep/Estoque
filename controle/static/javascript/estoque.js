var produtos = [["Código", "Descrição", "Custo", "Preço"]];
var entradas = [["Código", "Descrição", "Quantidade", "Data", "Motivo"]];
var saidas = [["Código", "Descrição", "Quantidade", "Data", "Motivo"]];
var estoque = [["Código", "Descrição", "Entradas", "Saídas", "Balanço", "Custo", "Custo Estimado", "Preço", "Venda Esperada"]];

function descProduto(){
  var produtos = window.parent.produtos;
  var id = document.getElementById("codigo").value;
  var desc;
  try {
    desc = produtos.filter(function(value){return value[0] == id;}) 
    document.getElementById("descricao").value = desc[0][1];
  }
  catch(err){
    alert("Código não localizado, verifique!");    
    return false;
  }

  return true;
}

function getIndexOfK(arr, k) {
  for (var i = 0; i < arr.length; i++) {
    var index = arr[i].indexOf(k);
    if (index > -1) {
      return i;
    }
  }
}

function updateEstoque(id, tipo, qtde){
  var estoque = window.parent.estoque;
  var ind = getIndexOfK(estoque, id);
  
  if ( tipo === "entrada" ){
    estoque[ind][2] = parseInt(estoque[ind][2]) + parseInt(qtde);
    estoque[ind][4] = parseInt(estoque[ind][2]) - parseInt(estoque[ind][3]);
    estoque[ind][6] = parseInt(estoque[ind][4]) * parseInt(estoque[ind][5]);
    estoque[ind][8] = parseInt(estoque[ind][4]) * parseInt(estoque[ind][7]);
  } else {
    estoque[ind][3] = (parseInt(estoque[ind][3]) - parseInt(qtde)) * -1;
    estoque[ind][4] = parseInt(estoque[ind][4]) - parseInt(qtde);
    estoque[ind][6] = parseInt(estoque[ind][4]) * parseInt(estoque[ind][5]);
    estoque[ind][8] = parseInt(estoque[ind][4]) * parseInt(estoque[ind][7]);
  }
  
}

function addEntrada(){
  entradas = window.parent.entradas;  
  if ( valEntrada() == false ){return false;}
  var entrada = [document.getElementById("codigo").value,
                document.getElementById("descricao").value,
                document.getElementById("quantidade").value,
                document.getElementById("data").value,
                document.getElementById("motivo").value];  
  window.parent.entradas.push(entrada);
  updateEstoque(document.getElementById("codigo").value, "entrada", document.getElementById("quantidade").value);
}

function addSaida(){
  var saidas = window.parent.saidas;   
  if ( valSaida() == false){return false;}
  var saida = [document.getElementById("codigo").value,
                document.getElementById("descricao").value,
                document.getElementById("quantidade").value,
                document.getElementById("data").value,
                document.getElementById("motivo").value];  
  window.parent.saidas.push(saida);
  updateEstoque(document.getElementById("codigo").value, "saida", document.getElementById("quantidade").value);
}


function addProduto(){
  produtos = window.parent.produtos;   
  var id = produtos.length;
  if ( valProduto() == false){return false;}
  var produto = [document.getElementById("codigo").value,
                document.getElementById("descricao").value,
                document.getElementById("custo").value,
                document.getElementById("preco").value];
  var est = [document.getElementById("codigo").value,
             document.getElementById("descricao").value,
             0,
             0, 
             0, 
             document.getElementById("custo").value, 
             0, 
             document.getElementById("preco").value, 
             0];

  window.parent.produtos.push(produto);
  window.parent.estoque.push(est);
}

function valProduto(){
  if(document.getElementById("codigo").value === ""){
    alert("O campo Código é obrigatório, verifique!");
    document.getElementById("codigo").focus();
    return false;
  }
  if(document.getElementById("descricao").value === ""){
    alert("O campo Descrição é obrigatório, verifique!");
    document.getElementById("descricao").focus();
    return false;
  }
  if(document.getElementById("custo").value === ""){
    alert("O campo Custo é obrigatório, verifique!");
    document.getElementById("custo").focus();
    return false;
  }
  if(document.getElementById("preco").value === ""){
    alert("O campo Preço é obrigatório, verifique!");
    document.getElementById("preco").focus();
    return false;
  }
  return true;
}

function valEntrada(){
  if(document.getElementById("codigo").value === ""){
    alert("O campo Código é obrigatório, verifique!");
    return false;
  }
  if(document.getElementById("quantidade").value === ""){
    alert("O campo Quantidade é obrigatório, verifique!");
    document.getElementById("quantidade").focus();
    return false;
  }
  if(document.getElementById("data").value === ""){
    alert("O campo Data é obrigatório, verifique!");
    document.getElementById("data").focus();
    return false;
  }
  return true;
}


function valSaida(){
  if(document.getElementById("codigo").value === ""){
    alert("O campo Código é obrigatório, verifique!");
    return false;
  }
  if(document.getElementById("quantidade").value === ""){
    alert("O campo Quantidade é obrigatório, verifique!");
    document.getElementById("quantidade").focus();
    return false;
  }
  if(document.getElementById("data").value === ""){
    alert("O campo Data é obrigatório, verifique!");
    document.getElementById("data").focus();
    return false;
  }
  return true;
}


function updateProduto(id){
  produtos = window.parent.produtos;  
  if ( valProduto() == false){return false;}
  produtos[id][0] = document.getElementById("codigo").value;
  produtos[id][1] = document.getElementById("descricao").value;
  produtos[id][2] = document.getElementById("custo").value;
  produtos[id][3] = document.getElementById("preco").value;  
}

function updateEntrada(id){
  entradas = window.parent.entradas;  
  if ( valEntrada() == false){return false;}
  entradas[id][0] = document.getElementById("codigo").value;
  entradas[id][1] = document.getElementById("descricao").value;
  entradas[id][2] = document.getElementById("quantidade").value;
  entradas[id][3] = document.getElementById("data").value;  
  entradas[id][3] = document.getElementById("motivo").value; 
}

function updateSaida(id){
  saidas = window.parent.saidas;  
  if ( valSaida() == false){return false;}
  saidas[id][0] = document.getElementById("codigo").value;
  saidas[id][1] = document.getElementById("descricao").value;
  saidas[id][2] = document.getElementById("quantidade").value;
  saidas[id][3] = document.getElementById("data").value;  
  saidas[id][4] = document.getElementById("motivo").value; 
}


function editProduto(id){
  window.open("produtos.html?id="+id,"iframe"); 
}

function editEntrada(id){
  window.open("entrada.html?id="+id,"iframe"); 
}

function editSaida(id){
  window.open("saida.html?id="+id,"iframe"); 
}


function delProduto(id){
  if (confirm("Confirma a exclusão do registro "+id+" ?")){
    window.parent.produtos.splice(parseInt(id), 1);
    window.open("vwProdutos.html","iframe");  
  }  
}

function delEntrada(id){
  if (confirm("Confirma a exclusão do registro "+id+" ?")){
    window.parent.entradas.splice(parseInt(id), 1);
    window.open("vwEntradas.html","iframe");  
  }  
}

function delSaida(id){
  if (confirm("Confirma a exclusão do registro "+id+" ?")){
    window.parent.Saidas.splice(parseInt(id), 1);
    window.open("vwSaidas.html","iframe");  
  }  
}


function loadForm(id){
  produtos = window.parent.produtos;
  document.getElementById("codigo").value = produtos[parseInt(id)][0];
  document.getElementById("descricao").value = produtos[parseInt(id)][1];
  document.getElementById("custo").value = produtos[parseInt(id)][2];
  document.getElementById("preco").value = produtos[parseInt(id)][3]; 
}

function loadFormEntrada(id){
  var entradas = window.parent.entradas;
  document.getElementById("codigo").value = entradas[parseInt(id)][0];
  document.getElementById("descricao").value = entradas[parseInt(id)][1];
  document.getElementById("quantidade").value = entradas[parseInt(id)][2];
  document.getElementById("data").value = entradas[parseInt(id)][3]; 
  document.getElementById("motivo").value = entradas[parseInt(id)][4];
}

function loadFormSaida(id){
  var saidas = window.parent.saidas;
  document.getElementById("codigo").value = saidas[parseInt(id)][0];
  document.getElementById("descricao").value = saidas[parseInt(id)][1];
  document.getElementById("quantidade").value = saidas[parseInt(id)][2];
  document.getElementById("data").value = saidas[parseInt(id)][3]; 
  document.getElementById("motivo").value = saidas[parseInt(id)][4];
}

function vwProdutos(){
  produtos = window.parent.produtos;  
  var totalRows = produtos.length;
  var divTbl = document.getElementById("tbl");
  var tbl = document.createElement("table");
  tbl.setAttribute("id", "grid"); 
  // creating rows
  for (var r = 0; r < totalRows; r++) {
    var row = document.createElement("tr");	     
    // create cells in row
    for (var c = 0; c < 4; c++) {    
      if (r === 0){
        var cell = document.createElement("th");
      } else {
        var cell = document.createElement("td");
      }
      		  
      cell.innerHTML = produtos[r][c];
      row.appendChild(cell);  
    }
    if ( r > 0) {
      //link editar
      var cell = document.createElement("td");		  
      cell.innerHTML = "<a href='javascript:editProduto(" + r  + ");'>Editar</a>";
      row.appendChild(cell);
      //link apagar
      var cell = document.createElement("td");		  
      cell.innerHTML = "<a href='javascript:delProduto(" + r  + ");'>Apagar</a>";
      row.appendChild(cell);
    } else if(r === 0){
      //coluna editar
      var cell = document.createElement("th");		  
      cell.innerHTML = "Editar";
      row.appendChild(cell);
      //coluna apagar
      var cell = document.createElement("th");		  
      cell.innerHTML = "Apagar";
      row.appendChild(cell);
    }
    
	  tbl.appendChild(row); // add the row to the end of the table body
  }    
  divTbl.appendChild(tbl); // appends <table> into <div1>
}


function vwEntradas(){
  entradas = window.parent.entradas;  
  var totalRows = entradas.length;
  var divTbl = document.getElementById("tbl");
  var tbl = document.createElement("table");
  tbl.setAttribute("id", "grid"); 
  // creating rows
  for (var r = 0; r < totalRows; r++) {
    var row = document.createElement("tr");	     
    // create cells in row
    for (var c = 0; c < 4; c++) {    
      if (r === 0){
        var cell = document.createElement("th");
      } else {
        var cell = document.createElement("td");
      }
      		  
      cell.innerHTML = entradas[r][c];
      row.appendChild(cell);  
    }
    if ( r > 0) {
      //link editar
      var cell = document.createElement("td");		  
      cell.innerHTML = "<a href='javascript:editEntrada(" + r  + ");'>Editar</a>";
      row.appendChild(cell);
      //link apagar
      var cell = document.createElement("td");		  
      cell.innerHTML = "<a href='javascript:delEntrada(" + r  + ");'>Apagar</a>";
      row.appendChild(cell);
    } else if(r === 0){
      //coluna editar
      var cell = document.createElement("th");		  
      cell.innerHTML = "Editar";
      row.appendChild(cell);
      //coluna apagar
      var cell = document.createElement("th");		  
      cell.innerHTML = "Apagar";
      row.appendChild(cell);
    }
    
	  tbl.appendChild(row); // add the row to the end of the table body
  }    
  divTbl.appendChild(tbl); // appends <table> into <div1>
}

function vwSaidas(){
  saidas = window.parent.saidas;  
  var totalRows = saidas.length;
  var divTbl = document.getElementById("tbl");
  var tbl = document.createElement("table");
  tbl.setAttribute("id", "grid"); 
  // creating rows
  for (var r = 0; r < totalRows; r++) {
    var row = document.createElement("tr");	     
    // create cells in row
    for (var c = 0; c < 4; c++) {    
      if (r === 0){
        var cell = document.createElement("th");
      } else {
        var cell = document.createElement("td");
      }
      		  
      cell.innerHTML = saidas[r][c];
      row.appendChild(cell);  
    }
    if ( r > 0) {
      //link editar
      var cell = document.createElement("td");		  
      cell.innerHTML = "<a href='javascript:editSaida(" + r  + ");'>Editar</a>";
      row.appendChild(cell);
      //link apagar
      var cell = document.createElement("td");		  
      cell.innerHTML = "<a href='javascript:delSaida(" + r  + ");'>Apagar</a>";
      row.appendChild(cell);
    } else if(r === 0){
      //coluna editar
      var cell = document.createElement("th");		  
      cell.innerHTML = "Editar";
      row.appendChild(cell);
      //coluna apagar
      var cell = document.createElement("th");		  
      cell.innerHTML = "Apagar";
      row.appendChild(cell);
    }
    
	  tbl.appendChild(row); // add the row to the end of the table body
  }    
  divTbl.appendChild(tbl); // appends <table> into <div1>
}


function vwEstoque(){
  estoque = window.parent.estoque;  
  var totalRows = estoque.length;
  var divTbl = document.getElementById("tbl");
  var tbl = document.createElement("table");
  tbl.setAttribute("id", "grid"); 
  // creating rows
  for (var r = 0; r < totalRows; r++) {
    var row = document.createElement("tr");	     
    // create cells in row
    for (var c = 0; c < 9; c++) {    
      if (r === 0){
        var cell = document.createElement("th");
      } else {
        var cell = document.createElement("td");
      }
      		  
      cell.innerHTML = estoque[r][c];
      row.appendChild(cell);  
    }
    
	  tbl.appendChild(row); // add the row to the end of the table body
  }    
  divTbl.appendChild(tbl); // appends <table> into <div1>
}
