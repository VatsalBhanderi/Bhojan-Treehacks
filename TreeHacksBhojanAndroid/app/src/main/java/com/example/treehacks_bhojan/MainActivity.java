package com.example.treehacks_bhojan;

import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private CardView breakfastCard;
    private CardView lunchCard;
    private CardView dinnerCard;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        breakfastCard = findViewById(R.id.breakfastCard);
        lunchCard = findViewById(R.id.lunchCard);
        dinnerCard = findViewById(R.id.dinnerCard);

        setCardClickListeners();

    }

    private void onCardClicked(){
        Toast.makeText(this, "Hello Devansh", Toast.LENGTH_SHORT).show();
    }

    private void setCardClickListeners(){

        breakfastCard.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                PopUpClass popUpClass = new PopUpClass();
                popUpClass.showPopupWindow(v);
            }
        });

        lunchCard.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                PopUpClass popUpClass = new PopUpClass();
                popUpClass.showPopupWindow(v);
            }
        });

        dinnerCard.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                PopUpClass popUpClass = new PopUpClass();
                popUpClass.showPopupWindow(v);
            }
        });


    }
}