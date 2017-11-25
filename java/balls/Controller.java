package balls;

import java.util.ArrayList;
import java.util.concurrent.Semaphore;

import javafx.event.ActionEvent;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.effect.BlendMode;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;

public class Controller {
  static int REC_X = 300;
  static int REC_Y = 200;
  static int REC_SIDE = 200;

  public Canvas canvas;
  ArrayList<Ball> balls;
  Semaphore semaphore;

  public void initialize() throws InterruptedException {
    semaphore = new Semaphore(1);
    balls = new ArrayList<>();
    drawAllBalls();
  }

  public void addBall(ActionEvent actionEvent) {
    balls.add(new Ball((int) canvas.getWidth(), (int) canvas.getHeight(), semaphore));
  }

  private void drawBall(int x, int y, int radius, Color color) {
    GraphicsContext graphicsConTemp = canvas.getGraphicsContext2D();
    graphicsConTemp.setGlobalBlendMode(BlendMode.DIFFERENCE);
    graphicsConTemp.setFill(color);
    graphicsConTemp.fillOval(x, y, radius, radius);
  }

  private boolean ifBallWasClicked(int mouseX, int mouseY, Ball ball) {
    return (Math.pow(mouseX - ball.ballPosX, 2) + Math.pow(mouseY - ball.ballPosY, 2) < Math.pow(ball.radius, 2));
  }

  public void mousePressed(MouseEvent mouseEvent) {
    for (Ball ball : balls) {
      if (ifBallWasClicked((int) mouseEvent.getX(), (int) mouseEvent.getY(), ball)) {
        if (mouseEvent.isPrimaryButtonDown()) {
          if (ball.isRunning) {
            ball.suspendBall();
          } else {
            ball.resumeBall();
          }
        } else if (mouseEvent.isSecondaryButtonDown()) {
          ball.stopBall();
          balls.remove(ball);
        }
      }
    }
  }

  private void drawAllBalls() throws InterruptedException {
    new Thread(() -> {
      while (true) {
        try {
          Thread.sleep(50);
        } catch (InterruptedException e) {
          e.printStackTrace();
        }
        clear();
        drawRect();
        for (Ball ball : balls) {
          drawBall(ball.ballPosX, ball.ballPosY, ball.radius, ball.color);
        }
      }
    }).start();

  }

  private void drawRect() {
    GraphicsContext graphicsCon = canvas.getGraphicsContext2D();
    graphicsCon.setStroke(Color.web("#E11212"));
    graphicsCon.setGlobalBlendMode(BlendMode.MULTIPLY);
    graphicsCon.strokeRect(REC_X, REC_Y, REC_SIDE, REC_SIDE);
  }

  private void clear() {
    GraphicsContext graphicsConTemp = canvas.getGraphicsContext2D();
    graphicsConTemp.setFill(Color.CORNSILK);
    graphicsConTemp.setGlobalBlendMode(BlendMode.SRC_OVER);
    graphicsConTemp.fillRect(0, 0, canvas.getWidth(), canvas.getHeight());
  }

}
