var targetContainer = document.getElementById("target-div");
var eventSource = new EventSource("/stream")
  eventSource.onmessage = function(e) {
  targetContainer.innerHTML = e.data;
};

var otherContainer = document.getElementById("other-div");
var eventSource2 = new EventSource("/1wire-devices")
  eventSource2.onmessage = function(e) {
  otherContainer.innerHTML = e.data;
};