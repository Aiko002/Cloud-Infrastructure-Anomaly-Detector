document.querySelector('.resolve').addEventListener('click', function() {
    alert('Anomaly acknowledged.');
    // Optionally, you can implement further logic here (like sending an acknowledgment to the backend).
  });
  
  document.querySelector('.more-info').addEventListener('click', function() {
    window.open('https://your-dashboard-url.com', '_blank');  // Redirects to a detailed dashboard or log page.
  });
  