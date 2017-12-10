package balls;

import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.effect.BlendMode;
import javafx.scene.paint.Color;

public class Box {
  double x, y, w, h;
  int counter = 0;

  Box(double x, double y, double w, double h) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
  }

  public void draw(GraphicsContext graph) {
    GraphicsContext graphicsCon = graph;
    graphicsCon.setStroke(Color.web("#E11212"));
    graphicsCon.setGlobalBlendMode(BlendMode.MULTIPLY);
    graphicsCon.strokeRect(x, y, w, h);
  }

  public boolean isInside(double ballx, double bally, double radius) {
    if (ballx + 0 > x - radius && ballx + 0 < (x + w) && bally + 0 > y - radius && bally + 0 < (y + h)) {
      return true;
    }
    return false;
  }

  public synchronized void enter() throws InterruptedException {
    if (counter > 0) {
      wait();
    }
    ++counter;
  }

  public synchronized void exit() {
    --counter;
    notify();
  }

}
