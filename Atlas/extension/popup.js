let isActive = false;
let anomalyCount1 = 0;
let anomalyCount2 = 0;
let anomalyCount3 = 0;
let anomalyInterval;

document.getElementById('activateBtn').addEventListener('click', () => {
  isActive = true;
  document.getElementById('activateBtn').style.display = 'none'; // Hide activate button
  document.getElementById('dashboard').style.display = 'block'; // Show dashboard

  // Start simulating anomaly detection
  anomalyInterval = setInterval(() => {
    // Randomly select a type of anomaly to simulate
    const anomalyType = Math.floor(Math.random() * 3) + 1; // Random number between 1 and 3
    if (anomalyType === 1) {
      anomalyCount1++;
      updateAnomalyCount('anomalyCount1', anomalyCount1);
    } else if (anomalyType === 2) {
      anomalyCount2++;
      updateAnomalyCount('anomalyCount2', anomalyCount2);
    } else {
      anomalyCount3++;
      updateAnomalyCount('anomalyCount3', anomalyCount3);
    }
  }, 3000); // Simulate a new anomaly every 3 seconds
});

document.getElementById('deactivateBtn').addEventListener('click', () => {
  isActive = false;
  clearInterval(anomalyInterval); // Stop anomaly simulation
  document.getElementById('dashboard').style.display = 'none'; // Hide dashboard
  document.getElementById('activateBtn').style.display = 'block'; // Show activate button
});

function updateAnomalyCount(countId, count) {
  const countDisplay = document.getElementById(countId);
  countDisplay.textContent = count;

  // Change text color to red if count changes
  if (count > 0) {
    countDisplay.style.color = 'red';
  }
}
