// Language Translation
function reloadpage(language) {
    window.location.href = language;
    location.reload();
}

if (window.location.hash === '') {
    window.location.hash = 'nl'
}
var language = {
        eng: {
            Titel: "Intake",
            Beschrijving: "This is where u can do your intake",
            Informatie: "Information",
            Informatie_beschrijving: "You will see a couple of questions. Answer every question with a number between 1 and 10.",
            Beoordeling: "1 meaning completely false, 10 meaning completely true",
            Volgende_Button1: "Next",
            Volgende_Button2: "Next",
            Volgende_Button3: "Next",
            Volgende_Button4: "Next",
            Volgende_Button5: "Next",
            Volgende_Button6: "Next",
            Volgende_Button7: "Next",
            Volgende_Button8: "Next",
            Volgende_Button9: "Next",
            Volgende_Button10: "Next",
            Volgende_Button11: "Next",
            Volgende_Button12: "Next",
            Volgende_Button13: "Next",
            Volgende_Button14: "Next",
            Volgende_Button15: "Next",
            Volgende_Button16: "Next",
            Volgende_Button17: "Next",
            Volgende_Button18: "Next",
            Volgende_Button19: "Next",
            Volgende_Button20: "Next",
            Volgende_Button21: "Next",
            Volgende_Button22: "Next",
            Volgende_Button23: "Next",
            Volgende_Button24: "Next",
            Volgende_Button25: "Next",
            Volgende_Button26: "Next",
            Volgende_Button27: "Next",
            Volgende_Button28: "Next",
            Volgende_Button29: "Next",
            Volgende_Button30: "Next",
            Vorige_Button1: "Previous",
            Vorige_Button2: "Previous",
            Vorige_Button3: "Previous",
            Vorige_Button4: "Previous",
            Vorige_Button5: "Previous",
            Vorige_Button6: "Previous",
            Vorige_Button7: "Previous",
            Vorige_Button8: "Previous",
            Vorige_Button9: "Previous",
            Vorige_Button10: "Previous",
            Vorige_Button11: "Previous",
            Vorige_Button12: "Previous",
            Vorige_Button13: "Previous",
            Vorige_Button14: "Previous",
            Vorige_Button15: "Previous",
            Vorige_Button16: "Previous",
            Vorige_Button17: "Previous",
            Vorige_Button18: "Previous",
            Vorige_Button19: "Previous",
            Vorige_Button20: "Previous",
            Vorige_Button21: "Previous",
            Vorige_Button22: "Previous",
            Vorige_Button23: "Previous",
            Vorige_Button24: "Previous",
            Vorige_Button25: "Previous",
            Vorige_Button26: "Previous",
            Vorige_Button27: "Previous",
            Vorige_Button28: "Previous",
            Vorige_Button29: "Previous",
            Vorige_Button30: "Previous",
            Submit_Button: "Submit",
            Vraag1_Header: "Question 1/30",
            Vraag2_Header: "Question 2/30",
            Vraag3_Header: "Question 3/30",
            Vraag4_Header: "Question 4/30",
            Vraag5_Header: "Question 5/30",
            Vraag6_Header: "Question 6/30",
            Vraag7_Header: "Question 7/30",
            Vraag8_Header: "Question 8/30",
            Vraag9_Header: "Question 9/30",
            Vraag10_Header: "Question 10/30",
            Vraag11_Header: "Question 11/30",
            Vraag12_Header: "Question 12/30",
            Vraag13_Header: "Question 13/30",
            Vraag14_Header: "Question 14/30",
            Vraag15_Header: "Question 15/30",
            Vraag16_Header: "Question 16/30",
            Vraag17_Header: "Question 17/30",
            Vraag18_Header: "Question 18/30",
            Vraag19_Header: "Question 19/30",
            Vraag20_Header: "Question 20/30",
            Vraag21_Header: "Question 21/30",
            Vraag22_Header: "Question 22/30",
            Vraag23_Header: "Question 23/30",
            Vraag24_Header: "Question 24/30",
            Vraag25_Header: "Question 25/30",
            Vraag26_Header: "Question 26/30",
            Vraag27_Header: "Question 27/30",
            Vraag28_Header: "Question 28/30",
            Vraag29_Header: "Question 29/30",
            Vraag30_Header: "Question 30/30",
            Vraag1: "I feel healthy",
            Vraag2: "My fitness is good",
            Vraag3: "I don't have pain",
            Vraag4: "I sleep well",
            Vraag5: "I eat well",
            Vraag6: "My memory is good",
            Vraag7: "I don't easily lose my concentration",
            Vraag8: "My mood is good",
            Vraag9: "I accept myself for being me",
            Vraag10: "I have control over my life",
            Vraag11: "My life has a meaning",
            Vraag12: "When I wake up I am ready for the day",
            Vraag13: "I have goals for the future",
            Vraag14: "I am sure I will reach those goals",
            Vraag15: "I accept the way life goes",
            Vraag16: "I enjoy life",
            Vraag17: "I feel happy",
            Vraag18: "I am happy with the way I feel",
            Vraag19: "I am happy with my living situation",
            Vraag20: "I can afford my expenses",
            Vraag21: "I have a social life",
            Vraag22: "I spend time with other people",
            Vraag23: "Whenever I feel down I have people who support me",
            Vraag24: "I have a feeling I'm part of something",
            Vraag25: "I spend my time in a good way",
            Vraag26: "I take care of myself",
            Vraag27: "I make sure I am and will stay healthy",
            Vraag28: "I know how to make an agenda",
            Vraag29: "I make sure I spend my money in the right way",
            Vraag30: "I know where and how to find help",
        },
        nl: {
            Titel: "Intake",
            Beschrijving: "Hier kunt u de intake enquete invullen",
            Informatie: "Informatie",
            Informatie_beschrijving: "Je zult hierna een aantal vragen te zien krijgen, geef bij elke vraag een antwoord geven tussen de 1 en 10",
            Beoordeling: "1 betekend helemaal niet waar, 10 betekend helemaal waar",
            Volgende_Button1: "Volgende",
            Volgende_Button2: "Volgende",
            Volgende_Button3: "Volgende",
            Volgende_Button4: "Volgende",
            Volgende_Button5: "Volgende",
            Volgende_Button6: "Volgende",
            Volgende_Button7: "Volgende",
            Volgende_Button8: "Volgende",
            Volgende_Button9: "Volgende",
            Volgende_Button10: "Volgende",
            Volgende_Button11: "Volgende",
            Volgende_Button12: "Volgende",
            Volgende_Button13: "Volgende",
            Volgende_Button14: "Volgende",
            Volgende_Button15: "Volgende",
            Volgende_Button16: "Volgende",
            Volgende_Button17: "Volgende",
            Volgende_Button18: "Volgende",
            Volgende_Button19: "Volgende",
            Volgende_Button20: "Volgende",
            Volgende_Button21: "Volgende",
            Volgende_Button22: "Volgende",
            Volgende_Button23: "Volgende",
            Volgende_Button24: "Volgende",
            Volgende_Button25: "Volgende",
            Volgende_Button26: "Volgende",
            Volgende_Button27: "Volgende",
            Volgende_Button28: "Volgende",
            Volgende_Button29: "Volgende",
            Volgende_Button30: "Volgende",
            Vorige_Button1: "Vorige",
            Vorige_Button2: "Vorige",
            Vorige_Button3: "Vorige",
            Vorige_Button4: "Vorige",
            Vorige_Button5: "Vorige",
            Vorige_Button6: "Vorige",
            Vorige_Button7: "Vorige",
            Vorige_Button8: "Vorige",
            Vorige_Button9: "Vorige",
            Vorige_Button10: "Vorige",
            Vorige_Button11: "Vorige",
            Vorige_Button12: "Vorige",
            Vorige_Button13: "Vorige",
            Vorige_Button14: "Vorige",
            Vorige_Button15: "Vorige",
            Vorige_Button16: "Vorige",
            Vorige_Button17: "Vorige",
            Vorige_Button18: "Vorige",
            Vorige_Button19: "Vorige",
            Vorige_Button20: "Vorige",
            Vorige_Button21: "Vorige",
            Vorige_Button22: "Vorige",
            Vorige_Button23: "Vorige",
            Vorige_Button24: "Vorige",
            Vorige_Button25: "Vorige",
            Vorige_Button26: "Vorige",
            Vorige_Button27: "Vorige",
            Vorige_Button28: "Vorige",
            Vorige_Button29: "Vorige",
            Vorige_Button30: "Vorige",
            Submit_Button: "Verzenden",
            Vraag1_Header: "Vraag 1/30",
            Vraag2_Header: "Vraag 2/30",
            Vraag3_Header: "Vraag 3/30",
            Vraag4_Header: "Vraag 4/30",
            Vraag5_Header: "Vraag 5/30",
            Vraag6_Header: "Vraag 6/30",
            Vraag7_Header: "Vraag 7/30",
            Vraag8_Header: "Vraag 8/30",
            Vraag9_Header: "Vraag 9/30",
            Vraag10_Header: "Vraag 10/30",
            Vraag11_Header: "Vraag 11/30",
            Vraag12_Header: "Vraag 12/30",
            Vraag13_Header: "Vraag 13/30",
            Vraag14_Header: "Vraag 14/30",
            Vraag15_Header: "Vraag 15/30",
            Vraag16_Header: "Vraag 16/30",
            Vraag17_Header: "Vraag 17/30",
            Vraag18_Header: "Vraag 18/30",
            Vraag19_Header: "Vraag 19/30",
            Vraag20_Header: "Vraag 20/30",
            Vraag21_Header: "Vraag 21/30",
            Vraag22_Header: "Vraag 22/30",
            Vraag23_Header: "Vraag 23/30",
            Vraag24_Header: "Vraag 24/30",
            Vraag25_Header: "Vraag 25/30",
            Vraag26_Header: "Vraag 26/30",
            Vraag27_Header: "Vraag 27/30",
            Vraag28_Header: "Vraag 28/30",
            Vraag29_Header: "Vraag 29/30",
            Vraag30_Header: "Vraag 30/30",
            Vraag1: "Ik voel mij gezond",
            Vraag2: "Ik voel mij fit",
            Vraag3: "Ik heb geen pijn",
            Vraag4: "Ik slaap goed",
            Vraag5: "Ik eet goed",
            Vraag6: "Mijn geheugen is goed",
            Vraag7: "Ik verlies niet snel mijn concentratie",
            Vraag8: "Mijn humeur is goed",
            Vraag9: "Ik accepteer mijzelf zoals ik ben",
            Vraag10: "Ik heb controle over mijn leven op het moment",
            Vraag11: "Mijn leven heeft zin",
            Vraag12: "Als ik wakker word, heb ik zin in de dag",
            Vraag13: "Ik heb (een) toekomstdoel(en)",
            Vraag14: "Ik vertrouw erop dat ik dit/deze doel(en) ga halen",
            Vraag15: "Ik accepteer hoe het leven loopt",
            Vraag16: "Ik geniet van het leven",
            Vraag17: "Ik voel mij gelukkig",
            Vraag18: "Ik zit lekker in mijn vel",
            Vraag19: "Ik ben tevreden met mijn woonsituatie",
            Vraag20: "Ik kan mijn vaste lasten betalen",
            Vraag21: "Ik heb contact met andere mensen",
            Vraag22: "Ik doe leuke dingen met mensen",
            Vraag23: "Als ik in een mindere periode zit, heb ik mensen die mij steunen",
            Vraag24: "Ik heb het gevoel dat ik erbij hoor",
            Vraag25: "Ik besteed mijn tijd goed",
            Vraag26: "Ik kan mijzelf goed verzorgen",
            Vraag27: "Ik zorg ervoor dat ik gezond ben en blijf",
            Vraag28: "Ik kan goed plannen",
            Vraag29: "Ik zorg ervoor dat ik goed met mijn geld omga",
            Vraag30: "Ik weet hoe en waar ik hulp kan zoeken als het wat minder gaat",
        }

    }
    // Define language via window hash
if (window.location.hash) {
    if (window.location.hash === "#eng") {
        Titel.textContent = language.eng.Titel;
        Beschrijving = language.eng.Beschrijving;
        Informatie.textContent = language.eng.Informatie;
        Informatie_beschrijving.textContent = language.eng.Informatie_beschrijving;
        Beoordeling.textContent = language.eng.Beoordeling;
        Volgende_Button1.textContent = language.eng.Volgende_Button1;
        Volgende_Button2.textContent = language.eng.Volgende_Button2;
        Volgende_Button3.textContent = language.eng.Volgende_Button3;
        Volgende_Button4.textContent = language.eng.Volgende_Button4;
        Volgende_Button5.textContent = language.eng.Volgende_Button5;
        Volgende_Button6.textContent = language.eng.Volgende_Button6;
        Volgende_Button7.textContent = language.eng.Volgende_Button7;
        Volgende_Button8.textContent = language.eng.Volgende_Button8;
        Volgende_Button9.textContent = language.eng.Volgende_Button9;
        Volgende_Button10.textContent = language.eng.Volgende_Button10;
        Volgende_Button11.textContent = language.eng.Volgende_Button11;
        Volgende_Button12.textContent = language.eng.Volgende_Button12;
        Volgende_Button13.textContent = language.eng.Volgende_Button13;
        Volgende_Button14.textContent = language.eng.Volgende_Button14;
        Volgende_Button15.textContent = language.eng.Volgende_Button15;
        Volgende_Button16.textContent = language.eng.Volgende_Button16;
        Volgende_Button17.textContent = language.eng.Volgende_Button17;
        Volgende_Button18.textContent = language.eng.Volgende_Button18;
        Volgende_Button19.textContent = language.eng.Volgende_Button19;
        Volgende_Button20.textContent = language.eng.Volgende_Button20;
        Volgende_Button21.textContent = language.eng.Volgende_Button21;
        Volgende_Button22.textContent = language.eng.Volgende_Button22;
        Volgende_Button23.textContent = language.eng.Volgende_Button23;
        Volgende_Button24.textContent = language.eng.Volgende_Button24;
        Volgende_Button25.textContent = language.eng.Volgende_Button25;
        Volgende_Button26.textContent = language.eng.Volgende_Button26;
        Volgende_Button27.textContent = language.eng.Volgende_Button27;
        Volgende_Button28.textContent = language.eng.Volgende_Button28;
        Volgende_Button29.textContent = language.eng.Volgende_Button29;
        Volgende_Button30.textContent = language.eng.Volgende_Button30;
        Vorige_Button1.textContent = language.eng.Vorige_Button1;
        Vorige_Button2.textContent = language.eng.Vorige_Button2;
        Vorige_Button3.textContent = language.eng.Vorige_Button3;
        Vorige_Button4.textContent = language.eng.Vorige_Button4;
        Vorige_Button5.textContent = language.eng.Vorige_Button5;
        Vorige_Button6.textContent = language.eng.Vorige_Button6;
        Vorige_Button7.textContent = language.eng.Vorige_Button7;
        Vorige_Button8.textContent = language.eng.Vorige_Button8;
        Vorige_Button9.textContent = language.eng.Vorige_Button9;
        Vorige_Button10.textContent = language.eng.Vorige_Button10;
        Vorige_Button11.textContent = language.eng.Vorige_Button11;
        Vorige_Button12.textContent = language.eng.Vorige_Button12;
        Vorige_Button13.textContent = language.eng.Vorige_Button13;
        Vorige_Button14.textContent = language.eng.Vorige_Button14;
        Vorige_Button15.textContent = language.eng.Vorige_Button15;
        Vorige_Button16.textContent = language.eng.Vorige_Button16;
        Vorige_Button17.textContent = language.eng.Vorige_Button17;
        Vorige_Button18.textContent = language.eng.Vorige_Button18;
        Vorige_Button19.textContent = language.eng.Vorige_Button19;
        Vorige_Button20.textContent = language.eng.Vorige_Button20;
        Vorige_Button21.textContent = language.eng.Vorige_Button21;
        Vorige_Button22.textContent = language.eng.Vorige_Button22;
        Vorige_Button23.textContent = language.eng.Vorige_Button23;
        Vorige_Button24.textContent = language.eng.Vorige_Button24;
        Vorige_Button25.textContent = language.eng.Vorige_Button25;
        Vorige_Button26.textContent = language.eng.Vorige_Button26;
        Vorige_Button27.textContent = language.eng.Vorige_Button27;
        Vorige_Button28.textContent = language.eng.Vorige_Button28;
        Vorige_Button29.textContent = language.eng.Vorige_Button29;
        Vorige_Button30.textContent = language.eng.Vorige_Button30;
        Submit_Button.textContent = language.eng.Submit_Button;
        Vraag1_Header.textContent = language.eng.Vraag1_Header;
        Vraag2_Header.textContent = language.eng.Vraag2_Header;
        Vraag3_Header.textContent = language.eng.Vraag3_Header;
        Vraag4_Header.textContent = language.eng.Vraag4_Header;
        Vraag5_Header.textContent = language.eng.Vraag5_Header;
        Vraag6_Header.textContent = language.eng.Vraag6_Header;
        Vraag7_Header.textContent = language.eng.Vraag7_Header;
        Vraag8_Header.textContent = language.eng.Vraag8_Header;
        Vraag9_Header.textContent = language.eng.Vraag9_Header;
        Vraag10_Header.textContent = language.eng.Vraag10_Header;
        Vraag11_Header.textContent = language.eng.Vraag11_Header;
        Vraag12_Header.textContent = language.eng.Vraag12_Header;
        Vraag13_Header.textContent = language.eng.Vraag13_Header;
        Vraag14_Header.textContent = language.eng.Vraag14_Header;
        Vraag15_Header.textContent = language.eng.Vraag15_Header;
        Vraag16_Header.textContent = language.eng.Vraag16_Header;
        Vraag17_Header.textContent = language.eng.Vraag17_Header;
        Vraag18_Header.textContent = language.eng.Vraag18_Header;
        Vraag19_Header.textContent = language.eng.Vraag19_Header;
        Vraag20_Header.textContent = language.eng.Vraag20_Header;
        Vraag21_Header.textContent = language.eng.Vraag21_Header;
        Vraag22_Header.textContent = language.eng.Vraag22_Header;
        Vraag23_Header.textContent = language.eng.Vraag23_Header;
        Vraag24_Header.textContent = language.eng.Vraag24_Header;
        Vraag25_Header.textContent = language.eng.Vraag25_Header;
        Vraag26_Header.textContent = language.eng.Vraag26_Header;
        Vraag27_Header.textContent = language.eng.Vraag27_Header;
        Vraag28_Header.textContent = language.eng.Vraag28_Header;
        Vraag29_Header.textContent = language.eng.Vraag29_Header;
        Vraag30_Header.textContent = language.eng.Vraag30_Header;
        Vraag1.textContent = language.eng.Vraag1;
        Vraag2.textContent = language.eng.Vraag2;
        Vraag3.textContent = language.eng.Vraag3;
        Vraag4.textContent = language.eng.Vraag4;
        Vraag5.textContent = language.eng.Vraag5;
        Vraag6.textContent = language.eng.Vraag6;
        Vraag7.textContent = language.eng.Vraag7;
        Vraag8.textContent = language.eng.Vraag8;
        Vraag9.textContent = language.eng.Vraag9;
        Vraag10.textContent = language.eng.Vraag10;
        Vraag11.textContent = language.eng.Vraag11;
        Vraag12.textContent = language.eng.Vraag12;
        Vraag13.textContent = language.eng.Vraag13;
        Vraag14.textContent = language.eng.Vraag14;
        Vraag15.textContent = language.eng.Vraag15;
        Vraag16.textContent = language.eng.Vraag16;
        Vraag17.textContent = language.eng.Vraag17;
        Vraag18.textContent = language.eng.Vraag18;
        Vraag19.textContent = language.eng.Vraag19;
        Vraag20.textContent = language.eng.Vraag20;
        Vraag21.textContent = language.eng.Vraag21;
        Vraag22.textContent = language.eng.Vraag22;
        Vraag23.textContent = language.eng.Vraag23;
        Vraag24.textContent = language.eng.Vraag24;
        Vraag25.textContent = language.eng.Vraag25;
        Vraag26.textContent = language.eng.Vraag26;
        Vraag27.textContent = language.eng.Vraag27;
        Vraag28.textContent = language.eng.Vraag28;
        Vraag29.textContent = language.eng.Vraag29;
        Vraag30.textContent = language.eng.Vraag30;
    }
    if (window.location.hash === "#nl") {
        Titel.textContent = language.nl.Titel;
        Beschrijving = language.nl.Beschrijving;
        Informatie.textContent = language.nl.Informatie;
        Informatie_beschrijving.textContent = language.nl.Informatie_beschrijving;
        Beoordeling.textContent = language.nl.Beoordeling;
        Volgende_Button1.textContent = language.nl.Volgende_Button1;
        Volgende_Button2.textContent = language.nl.Volgende_Button2;
        Volgende_Button3.textContent = language.nl.Volgende_Button3;
        Volgende_Button4.textContent = language.nl.Volgende_Button4;
        Volgende_Button5.textContent = language.nl.Volgende_Button5;
        Volgende_Button6.textContent = language.nl.Volgende_Button6;
        Volgende_Button7.textContent = language.nl.Volgende_Button7;
        Volgende_Button8.textContent = language.nl.Volgende_Button8;
        Volgende_Button9.textContent = language.nl.Volgende_Button9;
        Volgende_Button10.textContent = language.nl.Volgende_Button10;
        Volgende_Button11.textContent = language.nl.Volgende_Button11;
        Volgende_Button12.textContent = language.nl.Volgende_Button12;
        Volgende_Button13.textContent = language.nl.Volgende_Button13;
        Volgende_Button14.textContent = language.nl.Volgende_Button14;
        Volgende_Button15.textContent = language.nl.Volgende_Button15;
        Volgende_Button16.textContent = language.nl.Volgende_Button16;
        Volgende_Button17.textContent = language.nl.Volgende_Button17;
        Volgende_Button18.textContent = language.nl.Volgende_Button18;
        Volgende_Button19.textContent = language.nl.Volgende_Button19;
        Volgende_Button20.textContent = language.nl.Volgende_Button20;
        Volgende_Button21.textContent = language.nl.Volgende_Button21;
        Volgende_Button22.textContent = language.nl.Volgende_Button22;
        Volgende_Button23.textContent = language.nl.Volgende_Button23;
        Volgende_Button24.textContent = language.nl.Volgende_Button24;
        Volgende_Button25.textContent = language.nl.Volgende_Button25;
        Volgende_Button26.textContent = language.nl.Volgende_Button26;
        Volgende_Button27.textContent = language.nl.Volgende_Button27;
        Volgende_Button28.textContent = language.nl.Volgende_Button28;
        Volgende_Button29.textContent = language.nl.Volgende_Button29;
        Volgende_Button30.textContent = language.nl.Volgende_Button30;
        Vorige_Button1.textContent = language.nl.Vorige_Button1;
        Vorige_Button2.textContent = language.nl.Vorige_Button2;
        Vorige_Button3.textContent = language.nl.Vorige_Button3;
        Vorige_Button4.textContent = language.nl.Vorige_Button4;
        Vorige_Button5.textContent = language.nl.Vorige_Button5;
        Vorige_Button6.textContent = language.nl.Vorige_Button6;
        Vorige_Button7.textContent = language.nl.Vorige_Button7;
        Vorige_Button8.textContent = language.nl.Vorige_Button8;
        Vorige_Button9.textContent = language.nl.Vorige_Button9;
        Vorige_Button10.textContent = language.nl.Vorige_Button10;
        Vorige_Button11.textContent = language.nl.Vorige_Button11;
        Vorige_Button12.textContent = language.nl.Vorige_Button12;
        Vorige_Button13.textContent = language.nl.Vorige_Button13;
        Vorige_Button14.textContent = language.nl.Vorige_Button14;
        Vorige_Button15.textContent = language.nl.Vorige_Button15;
        Vorige_Button16.textContent = language.nl.Vorige_Button16;
        Vorige_Button17.textContent = language.nl.Vorige_Button17;
        Vorige_Button18.textContent = language.nl.Vorige_Button18;
        Vorige_Button19.textContent = language.nl.Vorige_Button19;
        Vorige_Button20.textContent = language.nl.Vorige_Button20;
        Vorige_Button21.textContent = language.nl.Vorige_Button21;
        Vorige_Button22.textContent = language.nl.Vorige_Button22;
        Vorige_Button23.textContent = language.nl.Vorige_Button23;
        Vorige_Button24.textContent = language.nl.Vorige_Button24;
        Vorige_Button25.textContent = language.nl.Vorige_Button25;
        Vorige_Button26.textContent = language.nl.Vorige_Button26;
        Vorige_Button27.textContent = language.nl.Vorige_Button27;
        Vorige_Button28.textContent = language.nl.Vorige_Button28;
        Vorige_Button29.textContent = language.nl.Vorige_Button29;
        Vorige_Button30.textContent = language.nl.Vorige_Button30;
        Submit_Button.textContent = language.nl.Submit_Button;
        Vraag1_Header.textContent = language.nl.Vraag1_Header;
        Vraag2_Header.textContent = language.nl.Vraag2_Header;
        Vraag3_Header.textContent = language.nl.Vraag3_Header;
        Vraag4_Header.textContent = language.nl.Vraag4_Header;
        Vraag5_Header.textContent = language.nl.Vraag5_Header;
        Vraag6_Header.textContent = language.nl.Vraag6_Header;
        Vraag7_Header.textContent = language.nl.Vraag7_Header;
        Vraag8_Header.textContent = language.nl.Vraag8_Header;
        Vraag9_Header.textContent = language.nl.Vraag9_Header;
        Vraag10_Header.textContent = language.nl.Vraag10_Header;
        Vraag11_Header.textContent = language.nl.Vraag11_Header;
        Vraag12_Header.textContent = language.nl.Vraag12_Header;
        Vraag13_Header.textContent = language.nl.Vraag13_Header;
        Vraag14_Header.textContent = language.nl.Vraag14_Header;
        Vraag15_Header.textContent = language.nl.Vraag15_Header;
        Vraag16_Header.textContent = language.nl.Vraag16_Header;
        Vraag17_Header.textContent = language.nl.Vraag17_Header;
        Vraag18_Header.textContent = language.nl.Vraag18_Header;
        Vraag19_Header.textContent = language.nl.Vraag19_Header;
        Vraag20_Header.textContent = language.nl.Vraag20_Header;
        Vraag21_Header.textContent = language.nl.Vraag21_Header;
        Vraag22_Header.textContent = language.nl.Vraag22_Header;
        Vraag23_Header.textContent = language.nl.Vraag23_Header;
        Vraag24_Header.textContent = language.nl.Vraag24_Header;
        Vraag25_Header.textContent = language.nl.Vraag25_Header;
        Vraag26_Header.textContent = language.nl.Vraag26_Header;
        Vraag27_Header.textContent = language.nl.Vraag27_Header;
        Vraag28_Header.textContent = language.nl.Vraag28_Header;
        Vraag29_Header.textContent = language.nl.Vraag29_Header;
        Vraag30_Header.textContent = language.nl.Vraag30_Header;
        Vraag1.textContent = language.nl.Vraag1;
        Vraag2.textContent = language.nl.Vraag2;
        Vraag3.textContent = language.nl.Vraag3;
        Vraag4.textContent = language.nl.Vraag4;
        Vraag5.textContent = language.nl.Vraag5;
        Vraag6.textContent = language.nl.Vraag6;
        Vraag7.textContent = language.nl.Vraag7;
        Vraag8.textContent = language.nl.Vraag8;
        Vraag9.textContent = language.nl.Vraag9;
        Vraag10.textContent = language.nl.Vraag10;
        Vraag11.textContent = language.nl.Vraag11;
        Vraag12.textContent = language.nl.Vraag12;
        Vraag13.textContent = language.nl.Vraag13;
        Vraag14.textContent = language.nl.Vraag14;
        Vraag15.textContent = language.nl.Vraag15;
        Vraag16.textContent = language.nl.Vraag16;
        Vraag17.textContent = language.nl.Vraag17;
        Vraag18.textContent = language.nl.Vraag18;
        Vraag19.textContent = language.nl.Vraag19;
        Vraag20.textContent = language.nl.Vraag20;
        Vraag21.textContent = language.nl.Vraag21;
        Vraag22.textContent = language.nl.Vraag22;
        Vraag23.textContent = language.nl.Vraag23;
        Vraag24.textContent = language.nl.Vraag24;
        Vraag25.textContent = language.nl.Vraag25;
        Vraag26.textContent = language.nl.Vraag26;
        Vraag27.textContent = language.nl.Vraag27;
        Vraag28.textContent = language.nl.Vraag28;
        Vraag29.textContent = language.nl.Vraag29;
        Vraag30.textContent = language.nl.Vraag30;
    }
}