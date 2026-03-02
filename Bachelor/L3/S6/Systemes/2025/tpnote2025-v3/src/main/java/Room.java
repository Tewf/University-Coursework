import java.awt.*;
import java.util.*;
import javax.swing.*;


public class Room extends JComponent {

	private static final long serialVersionUID = 1L;
	private java.util.List<Robot> robots;

	
	public Room() {
		robots = new ArrayList<>();
	}

	// méthode appelée par un thread gérant un robot lorsque ceci vient toucher le bord droit
	public void rightBorderTouched() {
		
	}

	// méthode appelée par un thread gérant un robot lorsque ceci vient toucher le bord gauche
	public void leftBorderTouched() {

	}

	// méthode appelée par un thread gérant un robot lorsque ceci vient toucher le bord bas
	public void bottomBorderTouched() {
		// TODO Auto-generated method stub
		
	}

	// méthode appelée par un thread gérant un robot lorsque ceci vient toucher le bord haut
	public void topBorderTouched() {
		// TODO Auto-generated method stub
		
	}

	// méthode appelée lors du clic sur Wake One
	public void wakeOne() {

	}
	
	// méthode appelée lors du clic sur Wake them all
	public void wakeAll() {

	}

	public void add(Robot r) {
		robots.add(r);
	}

	@Override
	public Dimension getPreferredSize() {
		return new Dimension(800, 600);
	}

	@Override
	protected void paintComponent(Graphics g) {
		Graphics2D g2d = (Graphics2D) g;
		RenderingHints rh = new RenderingHints(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
		g2d.setRenderingHints(rh);

		/*
		 * g2d.setColor(Color.green); g2d.fillRect(0, 0, getWidth()/4, getHeight());
		 */
		g2d.setColor(Color.red);
		robots.forEach(r -> {
			g2d.fillOval(r.getX(), r.getY(), r.getDiam(), r.getDiam());
		});
		super.paintComponent(g);
	}
	
	public void startRefresh() {
		new Thread(() -> {
			while (true) {
				try {
					Thread.sleep(20);
				} catch (InterruptedException e) {}
				repaint();
			}
		}).start();
	}
	
	
	public static JFrame buildFrame(Room s, int nbBalls) {
		JFrame f = new JFrame("Cours Système");
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.getContentPane().setLayout(new BorderLayout());
		f.getContentPane().add(s, BorderLayout.CENTER);
		
		
		JPanel jp = new JPanel();
		JButton btWakeOne = new JButton("Wake one");
		btWakeOne.addActionListener((e) -> s.wakeOne());
		JButton btWakeAll = new JButton("Wake them all");
		btWakeAll.addActionListener((e) -> s.wakeAll());
		jp.add(btWakeOne);
		jp.add(btWakeAll);
		f.getContentPane().add(jp, BorderLayout.SOUTH);
		f.pack();
		
		for (int i = 0; i < nbBalls; i++)
			new Thread(new Robot(s)).start();
		return f ;
	}

	public static void main(String[] args) {

		SwingUtilities.invokeLater(() -> {
			Room s1 = new Room();
			JFrame f1 = buildFrame(s1,25);
			f1.setVisible(true);
			s1.startRefresh();
		});
	}

	

}
