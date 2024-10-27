function navigateTo(feature) {
  if (feature === 'list') {
    window.location.href = 'list/';
  } else {
    alert('選択された機能が見つかりません。');
  }
}