
import java.util.ArrayList;
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.IOException;

public class PebbleGame {

  public static void main(String[] args) {
    if(args.length != 1) {
      System.out.println("Need edges input file");
      System.exit(0);
    }
    PebbleGraph graph = new PebbleGraph(args[0]);
    ArrayList<Vertex> vertices = graph.getVertices();
    try(BufferedWriter out = new BufferedWriter(new FileWriter("plot_graph.py"))) {
      out.write("import matplotlib.pyplot as plot\n");
      out.write("ax = plot.axes()\n");
      for(Vertex v : vertices) {
        out.write("plot.plot(" + ((v.getId()-1)%5) + "," + (4-(v.getId()-1)/5) +",'ko')\n" );
        out.write("ax.annotate(" + v.getId() + ",("+ ((v.getId()-1)%5) + "," 
            + (4-(v.getId()-1)/5) +"))\n" );
        
        ArrayList<Vertex> children = v.getChildren();
        for(Vertex child : children) {
          System.out.println(v.getId() + " " + child.getId());
          //out.write("ax.arrow(" + ((v.getId()-1)%5) + "," + (4-(v.getId()-1)/5) +"," 
          //    + ((child.getId()-1)%5) + "," + (4-(child.getId()-1)/5)+")\n" );
          out.write("plot.plot([" + ((v.getId()-1)%5) + "," + ((child.getId()-1)%5) +"],[" 
              + (4-(v.getId()-1)/5) + "," + (4-(child.getId()-1)/5)+"], 'k')\n" );
        }
      }
      out.write("plot.show()\n");
      Process p = Runtime.getRuntime().exec("python plot_graph.py");
    }
    catch (IOException ioe) {
      System.out.println("Quit being dumb");
    }
  }

}
