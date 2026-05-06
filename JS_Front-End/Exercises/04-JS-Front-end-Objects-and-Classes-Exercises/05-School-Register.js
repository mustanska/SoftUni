function solve(inputArray) {
    class Student {
        constructor(name, grade, score) {
            this.name = name;
            this.grade = grade;
            this.score = score;
        }
    }

    class Grade {
        constructor(number, listOfStudents, averageScore) {
            this.gradeNumber = number;
            this.listOfStudents = listOfStudents;
            this.averageScore = averageScore;
        }
    }

    let studentsInfo = getStudentObjects(inputArray);
    let grades = getGradeObjects(studentsInfo);
    printGrades(grades);

    function getStudentObjects(inputArray) {
        let studentsInfo = []

        for (const student of inputArray) {
            const [namePair, gradePair, scorePair] = student.split(', ');

            const name = namePair.split(': ')[1];
            const grade = Number(gradePair.split(': ')[1]);
            const score = Number(scorePair.split(': ')[1]);

            let studentObj = new Student(name, grade, score);
            studentsInfo.push(studentObj);
        }

        return studentsInfo;
    }

    function getSortedGrades(studentsInfo) {
        let gradeNumbers = []

        for (const student of studentsInfo) {
            if (!gradeNumbers.includes(student.grade)) {
                gradeNumbers.push(student.grade);
            }
        }

        return gradeNumbers.sort((a, b) => a - b);
    }



    function getGradeObjects(studentsInfo) {
        let sortedGrades = getSortedGrades(studentsInfo);
        let gradeObjectsArray = [];

        for (const grade of sortedGrades) {
            let students = [];
            let scores = [];

            for (const student of studentsInfo) {
                if (student.grade === grade && student.score >= 3) {
                    students.push(student.name);
                    scores.push(student.score);
                }
            }

            if (students.length > 0) {
                let averageScore = scores.reduce((a, b) => a + b) / scores.length;
                let gradeObj = new Grade(grade, students, averageScore.toFixed(2));

                gradeObjectsArray.push(gradeObj);
            }
        }
        
        return gradeObjectsArray;
    }

    function printGrades(grades) {
        for (const grade of grades) {
            let result = `${grade.gradeNumber + 1} Grade
List of students: ${grade.listOfStudents.join(', ')}
Average annual score from last year: ${grade.averageScore}`;
            console.log(result);
            console.log();
        }
    }
}

solve([
    "Student name: Mark, Grade: 8, Graduated with an average score: 4.75",
    "Student name: Ethan, Grade: 9, Graduated with an average score: 5.66",
    "Student name: George, Grade: 8, Graduated with an average score: 2.83",
    "Student name: Steven, Grade: 10, Graduated with an average score: 4.20",
    "Student name: Joey, Grade: 9, Graduated with an average score: 4.90",
    "Student name: Angus, Grade: 11, Graduated with an average score: 2.90",
    "Student name: Bob, Grade: 11, Graduated with an average score: 5.15",
    "Student name: Daryl, Grade: 8, Graduated with an average score: 5.95",
    "Student name: Bill, Grade: 9, Graduated with an average score: 6.00",
    "Student name: Philip, Grade: 10, Graduated with an average score: 5.05",
    "Student name: Peter, Grade: 11, Graduated with an average score: 4.88",
    "Student name: Gavin, Grade: 10, Graduated with an average score: 4.00"
]);
solve([
    'Student name: George, Grade: 5, Graduated with an average score: 2.75',
    'Student name: Alex, Grade: 9, Graduated with an average score: 3.66',
    'Student name: Peter, Grade: 8, Graduated with an average score: 2.83',
    'Student name: Boby, Grade: 5, Graduated with an average score: 4.20',
    'Student name: John, Grade: 9, Graduated with an average score: 2.90',
    'Student name: Steven, Grade: 2, Graduated with an average score: 4.90',
    'Student name: Darsy, Grade: 1, Graduated with an average score: 5.15'
]);