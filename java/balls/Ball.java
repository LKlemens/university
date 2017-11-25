package balls;

import java.util.Random;
import java.util.concurrent.Semaphore;

import javafx.scene.paint.Color;

public class Ball {
  private int ballSpeedX = 3;
  private int ballSpeedY = 4;
  int ballPosX, ballPosY;
  int radius;
  boolean semaphoreAcquired = false;
  boolean isRunning = true;
  Color color;
  Thread thread;
  Semaphore semaphore;

  Ball(int canvasWidth, int canvasHeight, Semaphore semaphore) {
    this.semaphore = semaphore;
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
    if (ballPosX + 0 > Controller.REC_X - radius && ballPosX + 0 < (Controller.REC_X + Controller.REC_SIDE)
        && ballPosY + 0 > Controller.REC_Y - radius
        && ballPosY + 0 < (Controller.REC_Y + Controller.REC_SIDE)) {
      if (!semaphoreAcquired) {
        semaphore.acquire();
        semaphoreAcquired = true;
      }
    } else if (semaphoreAcquired) {
      semaphore.release();
      semaphoreAcquired = false;
    }
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
