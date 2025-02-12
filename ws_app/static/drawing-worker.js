let canvas, ctx;
self.onmessage = function(e) {
  if (e.data.canvas) {
    canvas = e.data.canvas;
    canvas.width = e.data.width;
    canvas.height = e.data.height;
    ctx = canvas.getContext("2d");
    ctx.lineCap = "round";
  } else if (e.data.type === "start") {
    ctx.beginPath();
    ctx.moveTo(e.data.data.x, e.data.data.y);
    ctx.lineWidth = e.data.data.lineWidth;
    ctx.strokeStyle = e.data.data.color;
    ctx.globalAlpha = e.data.data.opacity;
    ctx.globalCompositeOperation = e.data.data.tool === "eraser" 
      ? "destination-out" 
      : "source-over";
  } else if (e.data.type === "draw") {
    ctx.lineTo(e.data.data.x, e.data.data.y);
    ctx.stroke();
  } else if (e.data.type === "end") {
    ctx.closePath();
    ctx.globalAlpha = 1;
  }
};
