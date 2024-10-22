// 画像プレビューを表示する関数
function previewImage() {
  const fileInput = document.getElementById('image-input');
  const preview = document.getElementById('image-preview');
  const file = fileInput.files[0];

  if (file) {
    const reader = new FileReader();
    reader.onload = function(e) {
      preview.src = e.target.result;
      preview.style.display = 'block';  // 画像を表示
    };
    reader.readAsDataURL(file);
  } else {
    alert('画像を選択してください！');
  }
}

// 画像をAIで解析する関数
function analyzeImage() {
  const resultSection = document.getElementById('result-section');
  const resultDisplay = document.getElementById('analysis-result');

  // ここに画像認識APIへのリクエストを実装することができます
  // 例: Google Cloud Vision APIやMicrosoft Azure Computer Vision APIとの連携

  // デモのため、仮の結果を表示
  resultDisplay.innerHTML = 'AIが画像を解析中です...';
  resultSection.style.display = 'block';

  // 実際には、APIの解析結果を取得して表示する
  setTimeout(function() {
    resultDisplay.innerHTML = '結果: この画像には猫が含まれています！';
  }, 2000); // 2秒後に結果を表示するデモ
}
