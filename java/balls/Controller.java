package balls;

import java.util.ArrayList;

import javafx.event.ActionEvent;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.effect.BlendMode;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;

public class Controller {
  int REC_X = 300;
  int REC_Y = 200;
  int REC_SIDE = 200;

  public Canvas canvas;
  ArrayList<Ball> balls;
  Box box;

  public void initialize() throws InterruptedException {
    balls = new ArrayList<>();
    box = new Box(REC_X, REC_Y, REC_SIDE, REC_SIDE);
    drawAllBalls();
  }

  public void addBall(ActionEvent actionEvent) {
    balls.add(new Ball((int) canvas.getWidth(), (int) canvas.getHeight(), box));
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
        box.draw(canvas.getGraphicsContext2D());
        for (Ball ball : balls) {
          ball.draw(canvas.getGraphicsContext2D());
        }
      }
    }).start();

  }

  private void clear() {
    GraphicsContext graphicsConTemp = canvas.getGraphicsContext2D();
    graphicsConTemp.setFill(Color.CORNSILK);
    graphicsConTemp.setGlobalBlendMode(BlendMode.SRC_OVER);
    graphicsConTemp.fillRect(0, 0, canvas.getWidth(), canvas.getHeight());
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


}
