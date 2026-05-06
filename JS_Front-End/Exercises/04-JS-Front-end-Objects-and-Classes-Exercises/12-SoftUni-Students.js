function solve(inputArray) {
    const courses = [];

    for (const row of inputArray) {
        if (row.includes(':')) {
            addCourse(row, courses);
        } else {
            addStudent(row, courses);
        }
    }

    const sortedCourses = sortCourses(courses);

    pritntInfo(sortedCourses);
    
    function addCourse(row, courses) {
        let [courseName, capacity] = row.split(': ');
        capacity = Number(capacity);

        const courseObj = {
            courseName,
            capacity,
            students: []
        }

        const courseNameArray = courses.filter(course => course.courseName === courseName)

        if(courseNameArray.length === 0) {
            courses.push(courseObj);
        } else {
            courses.map(course => {
                if (course.courseName === courseNameArray[0].courseName) {
                    course.capacity += capacity;
                }
            })
        }
    }

    function addStudent(row, courses) {
        let [studentInfo, courseName] = row.split(' joins ');
        let [studentArray, email] = studentInfo.split(' with email ');
        let [username, creditsString] = studentArray.split('[');
        let creditsCount = Number(creditsString.replace(']', ''));

        const studentObj = {
            username,
            creditsCount,
            email
        }

        courses.map(course => {
            if (course.courseName === courseName && course.capacity > 0) {
                course.students.push(studentObj);
                course.capacity -= 1;
            }
        })
    }

    function sortCourses(courses) {
        for (i = 0; i < courses.length; i++) {
            let courseEntries = Object.entries(courses[i]);
            courses.splice(i, 1, courseEntries);
        }
        
        courses.sort((a, b) => b[2][1].length - a[2][1].length);

        for (i = 0; i < courses.length; i++) {
            let course = Object.fromEntries(courses[i]);
            courses.splice(i, 1, course);
        }

        courses.map(course => sortStudents(course.students));

        return courses;
    }

    function sortStudents(students) {
        for (i = 0; i < students.length; i++) {
            let studentEntries = Object.entries(students[i]);
            students.splice(i, 1, studentEntries);
        }

        students.sort((a, b) => b[1][1] - a[1][1]);

        for (i = 0; i < students.length; i++) {
            let student = Object.fromEntries(students[i]);
            students.splice(i, 1, student);
        }
    }

    function pritntInfo(courses) {
        for (const course of courses) {
            console.log(`${course.courseName}: ${course.capacity} places left`);
            
            for (const student of course.students) {
                console.log(`--- ${student.creditsCount}: ${student.username}, ${student.email}`);
            }
        }
    }
}

solve([
    'JavaBasics: 2',
    'user1[25] with email user1@user.com joins C#Basics',
    'C#Advanced: 3', 
    'JSCore: 4',
    'user2[30] with email user2@user.com joins C#Basics',
    'user13[50] with email user13@user.com joins JSCore',
    'user1[25] with email user1@user.com joins JSCore',
    'user8[18] with email user8@user.com joins C#Advanced',
    'user6[85] with email user6@user.com joins JSCore',
    'JSCore: 2',
    'user11[3] with email user11@user.com joins JavaBasics',
    'user45[105] with email user45@user.com joins JSCore',
    'user007[20] with email user007@user.com joins JSCore',
    'user700[29] with email user700@user.com joins JSCore',
    'user900[88] with email user900@user.com joins JSCore'
]);
solve([
    'JavaBasics: 15',
    'user1[26] with email user1@user.com joins JavaBasics',
    'user2[36] with email user11@user.com joins JavaBasics',
    'JavaBasics: 5',
    'C#Advanced: 5',
    'user1[26] with email user1@user.com joins C#Advanced',
    'user2[36] with email user11@user.com joins C#Advanced',
    'user3[6] with email user3@user.com joins C#Advanced',
    'C#Advanced: 1',
    'JSCore: 8',
    'user23[62] with email user23@user.com joins JSCore'
])