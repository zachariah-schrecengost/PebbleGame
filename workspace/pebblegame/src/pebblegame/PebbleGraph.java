package pebblegame;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;

public class PebbleGraph {
  
  private Map<Integer, Vertex> vertices = new HashMap<Integer,Vertex>();
  private int unassignedPebbles;
  private ArrayList<Vertex> searched = new ArrayList<Vertex>();

  public PebbleGraph(String filename) {
    try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
      String str;
      while((str = br.readLine()) != null) {
        String[] split = str.split(",");
        Integer int0 = new Integer(split[0]);
        Integer int1 = new Integer(split[1]);
        Vertex v0 = vertices.get(int0);
        if(v0 == null) {
          v0 = new Vertex(int0);
          vertices.put(int0, v0);
          this.unassignedPebbles += 2;
        }
        Vertex v1 = vertices.get(int1);
        if(v1 == null) {
          v1 = new Vertex(int1);
          vertices.put(int1, v1);
          this.unassignedPebbles += 2;
        }
        if(v0.addChild(v1)) {
          --this.unassignedPebbles;
        }
        else {
          //if(findPebble(v0)) {
          //  v0.addChild(v1);
          //  --this.unassignedPebbles;
          //}
          if(collectPebbles(v0,v1)) {
            v0.addChild(v1);
            --this.unassignedPebbles;
          }
          else {
            v0.addBadChild(v1);
            System.out.println("Rigid Cluster Detected " + int0 + " " + int1);
            //break;
          }
        }
      }
    } catch(IOException ioe) {
      System.out.println("An IOException occurred. Don't be dumb.");
      ioe.printStackTrace();
    }   
    if(unassignedPebbles == 3) {
      System.out.println("GOOD");
    } 
    else if(unassignedPebbles < 3) {
      System.out.println("OVER");
    } 
    else if(unassignedPebbles > 3) {
      System.out.println("UNDER");
    } 
  }

  private boolean collectPebbles(Vertex v0, Vertex v1) {
    while(!v0.hasTwoPebbles()) {
      if(!this.findPebble(v0)) {
        return false;
      }
    }
    while(!v1.hasTwoPebbles()) {
      if(!this.findPebble(v1)) {
        return false;
      }
    }
    return true;
  }

  private boolean findPebble(Vertex vertex) {
    searched.add(vertex);	
    ArrayList<Vertex> children = vertex.getChildren();
    for(Vertex v : children) {
      if(searched.contains(v)) {
    	  continue;
      }
      searched.add(v);
      if(v.hasPebble()) {
        vertex.removeChild(v);
        v.addChildForPebble(vertex);
        searched.clear();
        return true;
      }
      else {
        return findPebble(v);
      }
    }
    return false;
  }
  
  public ArrayList<Vertex> getVertices(){
    return new ArrayList<Vertex>(vertices.values());
  }

}