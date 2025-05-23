int countSeniors(char** details, int detailsSize) {
    int target_age = 60;
    int res = 0;
    for (int i = 0; i < detailsSize; i++) {
        char ageStr[3];
        strncpy(ageStr, &details[i][11], 2);
        ageStr[2] = '\0';

        int age;
        sscanf(ageStr, "%d", &age);

        if (target_age < age){
            res += 1;
        }
    }

    return res;
}