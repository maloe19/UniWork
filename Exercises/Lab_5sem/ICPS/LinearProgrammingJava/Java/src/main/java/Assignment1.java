import org.ojalgo.OjAlgoUtils;
import org.ojalgo.optimisation.Expression;
import org.ojalgo.optimisation.ExpressionsBasedModel;
import org.ojalgo.optimisation.Optimisation;
import org.ojalgo.optimisation.Variable;

public class Assignment1 {
    public static void main(String[] args)
    {
        ExpressionsBasedModel model = new ExpressionsBasedModel();
        ///*
        //A:
        //z = 750x + 1000y
        Variable X = model.addVariable("Notebook").integer(true).weight(750);
        Variable Y = model.addVariable("Desktop").integer(true).weight(1000);

        //x+y<=10000
        Expression constraint1 = model.addExpression("Chips")
                .upper(10000)
                .set(X, 1)
                .set(Y, 1);
        
        //x + 2y <= 15.000
        Expression constraint2 = model.addExpression("Memory chip set")
                .upper(15000)
                .set(X, 1)
                .set(Y, 2);
        
        //4x + 3y <= 25.000
        Expression constraint3 = model.addExpression("Assembly minutes")
                .upper(25000)
                .set(X, 4)
                .set(Y, 3);
        
        //x >= 0
        Expression constraint4 = model.addExpression("x")
                .lower(0)
                .set(X, 1);
       
        //y >= 0            
        Expression constraint5 = model.addExpression("y")
                .lower(0)
                .set(Y, 1);
        //*/
        //----------------------------------------------------------------------
        /*
        //B:
        //z = -45x + -5y
        Variable X = model.addVariable("Cellphones").integer(true)
                .weight(-45);
        Variable Y = model.addVariable("Desktop").weight(-5);

        //50x + 24y <= 2400
        Expression constraint1 = model.addExpression("Machine A")
                .upper(2400)
                .set(X, 50)
                .set(Y, 24);
        
        //30x + 33y <= 2100
        Expression constraint2 = model.addExpression("Machine B")
                .upper(2100)
                .set(X, 30)
                .set(Y, 33);
        
        //x >= 45
        Expression constraint3 = model.addExpression("x")
                .lower(45)
                .set(X, 1);
        
        //y >= 5
        Expression constraint4 = model.addExpression("y")
                .lower(5)
                .set(Y, 1);
        
        //x >= 0
        Expression constraint5 = model.addExpression("x2")
                .lower(0)
                .set(X, 1);
       
        //y >= 0            
        Expression constraint6 = model.addExpression("y2")
                .lower(0)
                .set(Y, 1);
        */
        
        Optimisation.Result result = model.maximise();

        System.out.println("Result: " + result);
        System.out.println("Model: " + model);
    }
}
