package com.example.treehacks_bhojan;

import static androidx.core.app.ActivityCompat.startActivityForResult;

import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.provider.MediaStore;
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

        lunchCard.setOnClickListener(v -> {
            PopUpClass popUpClass = new PopUpClass();
            popUpClass.showPopupWindow(v);
        });

        dinnerCard.setOnClickListener(v -> {
            PopUpClass popUpClass = new PopUpClass();
            popUpClass.showPopupWindow(v);
        });
    }

    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        // Match the request 'pic id with requestCode
        if (requestCode == 1) {
            // BitMap is data structure of image file which store the image in memory
            Bitmap photo = (Bitmap) data.getExtras().get("data");
//            click_image_id.setImageBitmap(photo);
        }
    }

    public void openCamera(){
        Intent camera_intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        // Start the activity with camera_intent, and request pic id
        startActivityForResult(camera_intent, 1);
    }
}