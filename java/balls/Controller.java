package balls;

import java.util.ArrayList;
import java.util.Random;

import javafx.event.ActionEvent;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.Label;
import javafx.scene.effect.BlendMode;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;

public class Controller {

  public Label label;
  public Canvas canvas;
  private GraphicsContext graphicsCon;
  public ArrayList<Ball> balls;
  boolean startFlag;
  Random rand;
  Thread thread;

  public void initialize() {
    graphicsCon = canvas.getGraphicsContext2D();
    balls = new ArrayList<>();
    rand = new Random();
    startFlag = true;
  }

  public void addBall(ActionEvent actionEvent) throws InterruptedException {
    balls.add(new Ball((int) canvas.getWidth(), (int) canvas.getHeight()));
    if (startFlag) {
      drawAllBalls();
      startFlag = false;
    }
  }

  public void drawBall(int x, int y, int radius, Color color) {
    GraphicsContext graphicsConTemp = canvas.getGraphicsContext2D();
    graphicsConTemp.setGlobalBlendMode(BlendMode.MULTIPLY);
    graphicsConTemp.setFill(color);
    graphicsConTemp.fillOval(x, y, radius, radius);
  }

  private boolean ifBallWasClicked(int mouseX, int mouseY, Ball ball) {
    System.out.println("jestem w mouse " + mouseX + " " + mouseY);
    return Math.sqrt(mouseX - ball.getBallPos().getKey() + (mouseY - ball.getBallPos().getValue())) < ball.radius;
  }

  public void mousePressed(MouseEvent mouseEvent) {
    for (Ball ball : balls) {
      if (ifBallWasClicked((int) mouseEvent.getX(), (int) mouseEvent.getY(), ball)) {
        System.out.println("jestem w ifie");
        ball.suspendBall();
      }
    }
  }

  public void drawAllBalls() throws InterruptedException {
    thread = new Thread(() -> {
      while (true) {
        try {
          Thread.sleep(50);
        } catch (InterruptedException e) {
          e.printStackTrace();
        }
        clear();
        drawRect();
        for (Ball x : balls) {
          drawBall(x.getBallPos().getKey(), x.getBallPos().getValue(), x.radius, x.color);
        }
      }
    });
    thread.start();

  }

  /**
   * Draw rectangle
   *
   * @param actionEvent
   */
  public void drawRect() {
    graphicsCon.setStroke(Color.web("#E11212"));
    graphicsCon.setGlobalBlendMode(BlendMode.MULTIPLY);
    graphicsCon.strokeRect(300, canvas.getHeight() - 400, 200, 200);
  }

  private void clear() {
    GraphicsContext graphicsConTemp = canvas.getGraphicsContext2D();
    graphicsConTemp.setFill(Color.WHITE);
    graphicsConTemp.setGlobalBlendMode(BlendMode.SRC_OVER);
    graphicsConTemp.fillRect(0, 0, canvas.getWidth(), canvas.getHeight());
  }

}
