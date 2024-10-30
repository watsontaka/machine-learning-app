function navigateTo(feature) {
  if (feature === 'list') {
    window.location.href = "picture_classification/list/' %}";
  } else {
    alert('選択された機能が見つかりません。');
  }
}

function goBack() {
  window.history.back();
}