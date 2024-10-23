// 数値データを解析する関数
function analyzeData() {
  const dataInput = document.getElementById('data-input').value.trim();
  const resultSection = document.getElementById('result-section');
  const resultDisplay = document.getElementById('analysis-result');

  if (!dataInput) {
    alert('数値データを入力してください！');
    return;
  }

  // 数値データをカンマ区切りで分割し、数値の配列に変換
  const dataArray = dataInput.split(',').map(Number);

  if (dataArray.some(isNaN)) {
    alert('無効なデータが含まれています。数値のみをカンマ区切りで入力してください。');
    return;
  }

  // 仮の解析処理
  const sum = dataArray.reduce((acc, val) => acc + val, 0);
  const avg = sum / dataArray.length;
  const max = Math.max(...dataArray);
  const min = Math.min(...dataArray);

  // 結果を表示
  resultDisplay.innerHTML = `
    入力データ: ${dataArray.join(', ')}<br>
    合計: ${sum}<br>
    平均: ${avg.toFixed(2)}<br>
    最大値: ${max}<br>
    最小値: ${min}
  `;
  resultSection.style.display = 'block';
}
