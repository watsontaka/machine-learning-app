function navigateTo(feature) {
  if (feature === 'image-recognize') {
    window.location.href = 'image_recognize/';
  } else if (feature === 'numeric-analysis') {
    window.location.href = 'numeric_analysis/';
  } else if (feature === 'nlp') {
    window.location.href = 'nlp/';
  } else {
    alert('選択された機能が見つかりません。');
  }
}