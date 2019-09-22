var targetContainer = document.getElementById("target-div");
var eventSource = new EventSource("/stream")
  eventSource.onmessage = function(e) {
  targetContainer.innerHTML = e.data;
};