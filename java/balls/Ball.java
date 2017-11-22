package balls;

import java.util.Random;

import javafx.scene.paint.Color;
import javafx.util.Pair;

public class Ball {
  private int ballSpeedX = 3;
  private int ballSpeedY = 4;
  private int ballPosX;
  private int ballPosY;
  int radius;
  Color color;
  Thread thread;

  Ball(int canvasWidth, int canvasHeight) {
    setRandomRadiusAndPos(canvasWidth, canvasHeight);
    setRandomColor();
    thread = new Thread(() -> {
      while (true) {
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

  private void setRandomRadiusAndPos(int canvasWidth, int canvasHeight) {
    radius = new Random().nextInt(50) + 15;
    ballPosX = new Random().nextInt(canvasWidth - radius);
    ballPosY = new Random().nextInt(canvasHeight - radius);
  }

  private void setRandomColor() {
    Random rand = new Random();
    color = Color.rgb(rand.nextInt(256), rand.nextInt(256), rand.nextInt(256));
  }

  public Pair<Integer, Integer> getBallPos() {
    return new Pair<>(ballPosX, ballPosY);
  }

  public void suspendBall() {
    try {
      synchronized(thread) { // bez tego wywala wyjatek , a z synchronized freezuje apke
        this.wait();
      }
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
  }

  public void resumeBall() {
    thread.notify();
  }

}
