// not 100% sure how much of this code is mine and how much is stolen from the internet but the melody is mine for sure because it was a pain in the ass to do
// https://www.youtube.com/shorts/RZ13EMnoAX0 video of it doing its thing
#define NOTE_A4  440
#define NOTE_CS5 554
#define NOTE_D5  587
#define NOTE_E5  659
#define NOTE_FS5 740
#define NOTE_GS5 831
#define NOTE_A5  880
#define NOTE_B5  988
#define REST      0

int tempo = 100;

//set to pin speaker is in
int buzzer = 11;

// 4 = quarter note, 8 = eighth note, 16 = sixteeth note
int melody[] = {
  NOTE_A5, 16, REST, 16, NOTE_E5, 16, NOTE_D5, 16, NOTE_CS5, 8, REST, 16, NOTE_CS5, 16, NOTE_D5, 16, NOTE_E5, 16, NOTE_FS5, 16, NOTE_GS5, 16, NOTE_E5, 8, REST, 8,
  NOTE_FS5, 16, REST, 16, NOTE_E5, 16, NOTE_D5, 16, NOTE_CS5, 16, REST, 16, NOTE_CS5, 16, REST, 16, NOTE_B5, 16, REST, 16, NOTE_CS5, 16, REST, 16, NOTE_D5, 8, REST, 8,
  NOTE_A5, 16, REST, 16, NOTE_E5, 16, NOTE_D5, 16, NOTE_CS5, 8, REST, 8, NOTE_D5, 16, NOTE_E5, 16, NOTE_FS5, 16, NOTE_D5, 8, REST, 8,
  NOTE_FS5, 16, NOTE_E5, 16, NOTE_D5, 16, NOTE_CS5, 16, NOTE_B5, 16, NOTE_CS5, 16, NOTE_D5, 16, NOTE_FS5, 16, NOTE_E5, 16, NOTE_D5, 16, NOTE_CS5, 16, NOTE_B5, 16, NOTE_A5, 8, REST, 8,
  NOTE_CS5, 16, NOTE_B5, 16, NOTE_CS5, 16, REST, 16, NOTE_CS5, 16, REST, 16, NOTE_CS5, 16, NOTE_B5, 16, NOTE_CS5, 16, REST, 16, NOTE_B5, 16, REST, 16, NOTE_CS5, 8, REST, 8,
  NOTE_A5, 16, NOTE_B5, 16, NOTE_CS5, 16, NOTE_D5, 16, NOTE_CS5, 16, REST, 16, NOTE_B5, 16, REST, 16, NOTE_CS5, 4, REST, 4,
  NOTE_CS5, 16, NOTE_B5, 16, NOTE_CS5, 16, REST, 16, NOTE_CS5, 16, REST, 16, NOTE_D5, 16, NOTE_CS5, 16, NOTE_B5, 16, REST, 16, NOTE_E5, 16, REST, 16, NOTE_CS5,8, REST, 8,
  NOTE_CS5, 16, NOTE_B5, 16, NOTE_CS5, 16, NOTE_D5, 16, NOTE_CS5, 16, REST, 16, NOTE_A5, 16, REST, 16, NOTE_CS5, 4, REST, 4,
  NOTE_E5, 16, NOTE_D5, 16, NOTE_E5, 16, REST, 16, NOTE_E5, 16, REST, 16, NOTE_E5, 16, NOTE_D5, 16, NOTE_E5, 16, REST, 16, NOTE_FS5, 16, REST, 16, NOTE_E5, 8, REST, 8,
  NOTE_GS5, 16, REST, 16, NOTE_GS5, 16, NOTE_FS5, 16, NOTE_E5, 16, REST, 16, NOTE_D5, 16, REST, 16, NOTE_E5, 4, REST, 4,
  NOTE_CS5, 16, NOTE_B5, 16, NOTE_CS5, 16, REST, 16, NOTE_CS5, 16, REST, 16, NOTE_B5, 16, NOTE_CS5, 16, NOTE_D5, 16, REST, 16, NOTE_B5, 16, REST, 16, NOTE_CS5, 8, REST, 8,
  NOTE_CS5, 16, NOTE_B5, 16, NOTE_CS5, 16, NOTE_D5, 16, NOTE_CS5, 16, REST, 16, NOTE_A5, 16, REST, 16, NOTE_A4, 16, REST, 16, REST, 8, REST, 4,
};

int notes = sizeof(melody) / sizeof(melody[0]) / 2;

//more = slower, less = faster
int wholenote = (60000 * 4) / tempo;

void setup() {
  for (int thisNote = 0; thisNote < notes * 2; thisNote = thisNote + 2) {
    int noteDuration;
    int divider = melody[thisNote + 1];
    if (divider > 0) {
      noteDuration = (wholenote) / divider;
    } else if (divider < 0) {
      noteDuration = (wholenote) / abs(divider);
      noteDuration *= 1.5;
    }

    if (melody[thisNote] != REST) {
      tone(buzzer, melody[thisNote], noteDuration * 0.9);
    } else {
      noTone(buzzer);
    }

    delay(noteDuration);
    noTone(buzzer);
  }
}

void loop() {
}