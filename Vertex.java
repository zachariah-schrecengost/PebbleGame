
import java.util.ArrayList;

public class Vertex {

  private int id;
  private int numOfPebbles;
  private ArrayList<Vertex> children;
  private ArrayList<Vertex> badChildren;

  public Vertex(int id){
    this.id = id;
    this.numOfPebbles = 2;
    this.children = new ArrayList<Vertex>(2);
    this.badChildren = new ArrayList<Vertex>();
  }

  public boolean hasPebble() {
    return this.numOfPebbles != 0;
  }

  public boolean hasTwoPebbles() {
    return this.numOfPebbles == 2;
  }

  public boolean addChild(Vertex vertex) {
    //if(this.hasPebble()){
    if(this.hasTwoPebbles() && vertex.hasTwoPebbles()){
      this.children.add(vertex);
      --this.numOfPebbles;
      return true;
    } 
    return false;
  }

  public boolean removeChild(Vertex vertex) {
    if(this.children.remove(vertex)) {
      ++this.numOfPebbles;
      return true;
    }
    return false;
  }

  public ArrayList<Vertex> getChildren() {
    return this.children;
  }

  public void addBadChild(Vertex vertex) {
    this.badChildren.add(vertex);
  }

  public ArrayList<Vertex> getBadChildren() {
    return this.badChildren;
  }

  public int getId() {
    return this.id;
  }

}
