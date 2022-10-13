package org.example;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Filters;
import org.bson.Document;

import java.util.Arrays;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main(String[] args) {
        Logger.getLogger("").setLevel(Level.WARNING);

        String connnectionString = "mongodb://localhost:27017";
        MongoClient mongoClient = MongoClients.create(connnectionString);
        MongoDatabase mongoDatabase = mongoClient.getDatabase("MyStore");
        MongoCollection ProdutcsColletion = mongoDatabase.getCollection("Produtcs");

        Document store = new Document("_id", 5)
                .append("store_name", "TundraMotors")
                .append("founded_date", 1995)
                .append("inventory", Arrays.asList("Kia", "Fiat"))
                .append("employees", Arrays.asList("Jake", "Bob", "Jane"));
        System.out.println(store.toJson());

        ProdutcsColletion.insertOne(store);

        Document result = (Document) ProdutcsColletion.find(Filters.eq("store_name","TundraMotors")).first();
        System.out.println(result.toJson());

    }
}
