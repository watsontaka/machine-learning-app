let dataList = [];
let currentId = 1;

// データを追加する関数
function addData() {
  const dataInput = document.getElementById('data-input');
  const dataText = dataInput.value.trim();

  if (dataText === "") {
    alert("データを入力してください！");
    return;
  }

  // 新しいデータオブジェクトを作成
  const newData = {
    id: currentId++,
    text: dataText
  };

  // データリストに追加
  dataList.push(newData);
  dataInput.value = ""; // 入力フィールドをクリア
  renderTable(); // テーブルを再描画
}

// データを表示する関数
function renderTable() {
  const dataBody = document.getElementById('data-body');
  dataBody.innerHTML = ""; // テーブルをクリア

  // データリストをテーブルに表示
  dataList.forEach(data => {
    const row = document.createElement('tr');

    // ID列
    const idCell = document.createElement('td');
    idCell.textContent = data.id;
    row.appendChild(idCell);

    // データ内容列
    const textCell = document.createElement('td');
    textCell.textContent = data.text;
    row.appendChild(textCell);

    // 操作列（編集・削除ボタン）
    const actionCell = document.createElement('td');
    const editBtn = document.createElement('button');
    editBtn.textContent = "編集";
    editBtn.classList.add('action-btn');
    editBtn.onclick = () => editData(data.id);

    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = "削除";
    deleteBtn.classList.add('action-btn');
    deleteBtn.onclick = () => deleteData(data.id);

    actionCell.appendChild(editBtn);
    actionCell.appendChild(deleteBtn);
    row.appendChild(actionCell);

    dataBody.appendChild(row);
  });
}

// データを編集する関数
function editData(id) {
  const newDataText = prompt("新しいデータ内容を入力してください:");
  if (newDataText === null || newDataText.trim() === "") return;

  const dataIndex = dataList.findIndex(data => data.id === id);
  if (dataIndex !== -1) {
    dataList[dataIndex].text = newDataText.trim();
    renderTable(); // テーブルを再描画
  }
}

// データを削除する関数
function deleteData(id) {
  dataList = dataList.filter(data => data.id !== id);
  renderTable(); // テーブルを再描画
}

function goBack() {
  window.history.back();
}
