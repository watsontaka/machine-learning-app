function navigateTo(feature) {
  if (feature === 'image-recognize') {
    window.location.href = 'image_recognize/';
  } else if (feature === 'numeric-analysis') {
    window.location.href = 'numeric-analysis.html';
  } else if (feature === 'nlp') {
    window.location.href = 'nlp.html';
  } else {
    alert('選択された機能が見つかりません。');
  }
}