package balls;

import java.util.Random;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.effect.BlendMode;
import javafx.scene.paint.Color;

public class Ball {
  private int ballSpeedX = 3;
  private int ballSpeedY = 4;
  int ballPosX, ballPosY;
  int radius;
  boolean isRunning = true;
  boolean isInside = false;
  Color color;
  Thread thread;
  Box monitor;

  Ball(int canvasWidth, int canvasHeight, Box monitor) {
    this.monitor = monitor;
    setRandomRadiusAndPos(canvasWidth, canvasHeight);
    setRandomColor();
    thread = new Thread(() -> {
      while (true) {
        try {
          ballIsInRectanle();
        } catch (InterruptedException e) {
          e.printStackTrace();
        }
        ballPosX += ballSpeedX;
        ballPosY += ballSpeedY;
        try {
          Thread.sleep(30);
        } catch (InterruptedException e) {
          e.printStackTrace();
        }
        if (ballPosX + radius >= canvasWidth) {
          ballSpeedX = -ballSpeedX;
        } else if (ballPosX < 0) {
          ballSpeedX = -ballSpeedX;
        } else if (ballPosY + radius >= canvasHeight) {
          ballSpeedY = -ballSpeedY;
        } else if (ballPosY < 0) {
          ballSpeedY = -ballSpeedY;
        }
      }
    });
    thread.start();
  }

  private void ballIsInRectanle() throws InterruptedException {
    if (monitor.isInside(ballPosX, ballPosY, radius)) {
      if (!isInside) {
        isInside = true;
        monitor.enter();
      }
    } else if (isInside) {
      isInside = false;
      monitor.exit();
    }
  }

  private void setRandomRadiusAndPos(int canvasWidth, int canvasHeight) {
    radius = new Random().nextInt(50) + 15;
    ballPosX = new Random().nextInt(canvasWidth - radius);
    ballPosY = new Random().nextInt(canvasHeight - radius);
  }

  public void draw(GraphicsContext grap) {
    GraphicsContext graphicsConTemp = grap;
    graphicsConTemp.setGlobalBlendMode(BlendMode.DIFFERENCE);
    graphicsConTemp.setFill(color);
    graphicsConTemp.fillOval(ballPosX, ballPosY, radius, radius);
  }

  private void setRandomColor() {
    Random rand = new Random();
    color = Color.rgb(rand.nextInt(256), rand.nextInt(256), rand.nextInt(256));
  }

  void suspendBall() {
    thread.suspend();
    isRunning = false;
  }

  void resumeBall() {
    thread.resume();
    isRunning = true;
  }

  void stopBall() {
    thread.stop();
  }

}
