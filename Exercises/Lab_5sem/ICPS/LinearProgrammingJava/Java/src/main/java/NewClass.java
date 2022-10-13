/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Bruger
 */
import java.awt.*;
import java.awt.geom.*;
import static java.lang.Math.*;

public class NewClass {
    
/*
//Bearbejdelse
public static y(double ya, double yb, double yc, double yd){
	double y1 = yb - ya;
    double y2 = ya - yc;
    double y3 = yd - yc;
    double yp = ya + y1;
    
    double ay = ya;
    double by = yb;
    double cy = yc;
    double dy = yd;
}

public static x(double xa, double xb, double xc, double xd){
	double x1 = xb - xa;
    double x2 = xa - xc;
    double x3 = xd - xc;
    double xp = xa + x1;
    
    double ax = xa;
    double bx = xb;
    double cx = xc;
    double dx = xd;
}

public static isva(){ //intersectVarAttribute
		    double denom = (x.x1 * y.y3 - y.y1 * x.x3);
	        double rnum = (y.y2 * x.x3 - x.x3 * y.y3);
			double r = rnum / denom;
	        double snum = (y.y2 * x.x1 - x.x2 * y.y1);
	        double s = snum / denom;
            double px = xp * r;
	        double py = yp * r;
}

public static Point2D.Double intersectPre() { 
	        if (isva.denom == 0.0) || (isva.rnum == 0.0) { 
	        	if ((x.ax < x.bx && (x.bx < x,cx || x.bx < x.dx)) || (x.ax > x.bx && (x.bx > x.cx || x.bx > x.dx))) {
	                return new Point2D.Double(x.bx, y.by);
	            } else {
	                return new Point2D.Double(x.ax, y.ay);}
	        } else {
	            return null;}

public static Point2D.Double intersect(double limit) {
			intersectPre;
	        isva.r || isva.snum || isva.s;
	        if (0.0 <= r && r <= 1.0 && 0.0 <= s && s <= 1.0) {
	            isva.px || isva.py;
	            return new Point2D.Double(px, py);
	        } else {
				isva.px || isva.py;
	            if (length(x.ax, y.ay, px, py) <= limit || length(x.bx, y.by, px, py) <= limit || length(x.cx, y.cy, px, py) <= limit || length(x.dx, y.dy, px, py) <= limit) {
	                return new Point2D.Double(px, py);}
	            return null;}}
    
public static Point2D.Double intersect() { 
intersectPre;
isva.r || isva.snum || isva.s;
 if (0.0 <= r && r <= 1.0 && 0.0 <= s && s <= 1.0) {
isva.px || isva.py;
            return new Point2D.Double(px, py);
        } else {
            return null;
        }
    }

public static yi(int ya, int yb, int yc, int yd){
	int y1 = yb - ya;
    int y2 = ya - yc;
   int y3 = yd - yc;
    int yp = ya + y1;
    
   int ay = ya;
    int by = yb;
    int cy = yc;
    int dy = yd;
}

public static xi(int xa, int xb, int xc, int xd){
	int x1 = xb - xa;
    int x2 = xa - xc;
    int x3 = xd - xc;
    int xp = xa + x1;
    
    int ax = xa;
    int bx = xb;
    int cx = xc;
    int dx = xd;
}

public static isvai(){ //intersectVarAttribute
		    double denom = (xi.x1 * yi.y3 - yi.y1 * xi.x3);
	        double rnum = (yi.y2 * xi.x3 - xi.x3 * yi.y3);
			double r = rnum / denom;
	        double snum = (yi.y2 * xi.x1 - xi.x2 * yi.y1);
	        double s = snum / denom;
            int px = xp * r;
	        int py = yp * r;
}

public static Point2D.Double intersectPrei() { 
	        if (isvai.denom == 0.0) || (isvai.rnum == 0.0) { 
	        	if ((xi.ax < xi.bx && (xi.bx < xi,cx || xi.bx < xi.dx)) || (xi.ax > xi.bx && (xi.bx > xi.cx || xi.bx > xi.dx))) {
	                return new Point2D.Double(xi.bx, yi.by);
	            } else {
	                return new Point2D.Double(xi.ax, yi.ay);}
	        } else {
	            return null;}

public static Point intersect() { 
	intersectPrei;
isvai.r || isvai.snum || isvai.s;
 if (0.0 <= r && r <= 1.0 && 0.0 <= s && s <= 1.0) {
isvai.px || isvai.py;
            return new Point2D.Double(px, py);
        } else {
            return null;
        }
    }
*/
//------------------------------------------------------------------------------

//Rettelse
    //--------------------------------------------------------------------------
    //public static Point2D.Double y(double ya, double yb, double yc, double yd){
    double ya; 
    double yb; 
    double yc; 
    double yd;
    
    double y1 = yb - ya;
    double y2 = ya - yc;
    double y3 = yd - yc;
    double yp = ya + y1;
  
    double ay = ya;
    double by = yb;
    double cy = yc;
    double dy = yd;
    
    //return null;
//}

//public static Point2D.Double x(double xa, double xb, double xc, double xd){
    double xa; 
    double xb; 
    double xc; 
    double xd;
    
    double x1 = xb - xa;
    double x2 = xa - xc;
    double x3 = xd - xc;
    double xp = xa + x1;
    
    double ax = xa;
    double bx = xb;
    double cx = xc;
    double dx = xd;
    
    //return null;
//}

//public static yi(int ya, int yb, int yc, int yd){
    int yai; 
    int ybi; 
    int yci; 
    int ydi;
        
    int y1i = ybi - yai;
    int y2i = yai - yci;
    int y3i = ydi - yci;
    int ypi = yai + y1i;
    
    int ayi = yai;
    int byi = ybi;
    int cyi = yci;
    int dyi = ydi;
//}

//public static xi(int xa, int xb, int xc, int xd){
    int xai;
    int xbi;
    int xci;    
    int xdi;
        
    int x1i = xbi - xai;
    int x2i = xai - xci;
    int x3i = xdi - xci;
    int xpi = xai + x1i;
    
    int axi = xai;
    int bxi = xbi;
    int cxi = xci;
    int dxi = xdi;
//}    
    
//public static Point2D.Double isva(){ //intersectVarAttribute
    //double denom = (x.x1 * y.y3 - y.y1 * x.x3);
    double denom = (x1 * y3 - y1 * x3);
    //double rnum = (y.y2 * x.x3 - x.x3 * y.y3);
    double rnum = (y2 * x3 - x3 * y3);
    double r = rnum / denom;
    //double snum = (y.y2 * x.x1 - x.x2 * y.y1);
    double snum = (y2 * x1 - x2 * y1);
    double s = snum / denom;
    double px = xp * r;
    double py = yp * r;
    
    int pxi = (int)(xp * r);
    int pyi = (int)(yp * r);
                //return null;
//}

public Point2D.Double intersectPre() { 
    //if (isva.denom == 0.0) || (isva.rnum == 0.0) { 
    if ((denom == 0.0) && (rnum == 0.0)) {
        //if ((x.ax < x.bx && (x.bx < x,cx || x.bx < x.dx)) || (x.ax > x.bx && (x.bx > x.cx || x.bx > x.dx))) {
        if ((ax < bx && (bx < cx || bx < dx)) || (ax > bx && (bx > cx || bx > dx))) {
            //return new Point2D.Double(x.bx, y.by);
            return new Point2D.Double(bx, by);
        } else {
            //return new Point2D.Double(x.ax, y.ay);}
            return new Point2D.Double(ax, ay);
        }} else {
            return null;
        }
}

public Point2D.Double intersect() { 
    intersectPre();
    //isva.r || isva.snum || isva.s;
    //double r, snum, s;
    if (0.0 <= r && r <= 1.0 && 0.0 <= s && s <= 1.0) {
        //isva.px || isva.py;
        //double px, py;
        return new Point2D.Double(px, py);
    } else {
        return null;
    }
}

public Point2D.Double intersectPrei() { 
    if ((denom == 0.0) && (rnum == 0.0)) { 
	if ((axi < bxi && (bxi < cxi || bxi < dxi)) || (axi > bxi && (bxi > cxi || bxi > dxi))) {
	    return new Point2D.Double(bxi, byi);
	} else {
            return new Point2D.Double(axi, ayi);}
	} else {
	    return null;}
        }

public Point2D.Double intersecti() { 
    intersectPrei();
    //double r, snum, s;
    if (0.0 <= r && r <= 1.0 && 0.0 <= s && s <= 1.0) {
        //int pxi, pyi;
        return new Point2D.Double(pxi, pyi);
    } else {
        return null;
    }
}

public Point2D.Double intersect(double limit) {
    intersectPre();
    //isva.r || isva.snum || isva.s;
    //double r, snum, s; 
    if (0.0 <= r && r <= 1.0 && 0.0 <= s && s <= 1.0) {
        //isva.px || isva.py;
            //double px, py;
	    return new Point2D.Double(px, py);
	} else {
            //isva.px || isva.py;
            //double px, py;
        
        //if (length(x.ax, y.ay, px, py) <= limit || length(x.bx, y.by, px, py) <= limit || length(x.cx, y.cy, px, py) <= limit || length(x.dx, y.dy, px, py) <= limit) {
        if (length(ax, ay, px, py) <= limit || length(bx, by, px, py) <= limit || length(cx, cy, px, py) <= limit || length(dx, dy, px, py) <= limit) {
	    return new Point2D.Double(px, py);
        }
        return null;
    }
}	
/*
public static isvai(){ //intersectVarAttribute
		    double denom = (xi.x1 * yi.y3 - yi.y1 * xi.x3);
	        double rnum = (yi.y2 * xi.x3 - xi.x3 * yi.y3);
			double r = rnum / denom;
	        double snum = (yi.y2 * xi.x1 - xi.x2 * yi.y1);
	        double s = snum / denom;
            int px = xp * r;
	        int py = yp * r;
}
*/




    //--------------------------------------------------------------------------    

}
