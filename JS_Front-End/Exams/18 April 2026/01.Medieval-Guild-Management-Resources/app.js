function solve(inputArr) {
    const guildMembersCount = Number(inputArr.shift());

    const guildMembers = {}

    for (let i = 0; i < guildMembersCount; i++) {
        const [memberName, role, skillsAsString] = inputArr.shift().split(' ');
        skills = skillsAsString.split(',');

        guildMembers[memberName] = {role, skills};
    }

    let commandLine = inputArr.shift();

    while (commandLine !== 'End') {
        const[command, memberName, ...args] = commandLine.split(' / ');

        switch (command) {
            case 'Perform':
                const [role, skill] = args;

                if (guildMembers[memberName].role === role && guildMembers[memberName].skills.includes(skill)) {
                    console.log(`${memberName} has successfully performed the skill: ${skill}!`);
                } else {
                    console.log(`${memberName} cannot perform the skill: ${skill}.`);
                }

                break;
            case 'Reassign':
                const newRole = args[0];

                guildMembers[memberName].role = newRole;
                console.log(`${memberName} has been reassigned to: ${newRole}`);
                
                break;
            case 'Learn Skill':
                const newSkill = args[0];

                if (guildMembers[memberName].skills.includes(newSkill)) {
                    console.log(`${memberName} already knows the skill: ${newSkill}.`);
                    break;
                }

                guildMembers[memberName].skills.push(newSkill);
                console.log(`${memberName} has learned a new skill: ${newSkill}.`);
                
                break;
        }

        commandLine = inputArr.shift();
    }

    for (const memberName in guildMembers) {
        let result = `Guild Member: ${memberName}, `;
        result += `Role: ${guildMembers[memberName].role}, `;
        result += `Skills: ${guildMembers[memberName].skills.sort((a, b) => a.localeCompare(b)).join(', ')}`;

        console.log(result);
    }
}

solve([
    "3",
    "Arthur warrior swordsmanship,shield",
    "Merlin mage fireball,teleport",
    "Gwen healer healing,alchemy",
    "Perform / Arthur / warrior / swordsmanship",
    "Perform / Merlin / warrior / fireball",
    "Learn Skill / Gwen / purification",
    "Perform / Gwen / healer / purification",
    "Reassign / Merlin / healer",
    "Perform / Merlin / healer / teleport",
    "End"
]);
solve([
    "4",
    "Lancelot knight jousting,swordplay",
    "Morgana sorceress dark_magic,illusion",
    "Robin archer archery,stealth",
    "Galahad paladin healing,swordplay",
    "Perform / Robin / archer / archery",
    "Perform / Morgana / knight / illusion",
    "Learn Skill / Lancelot / swordplay",
    "Learn Skill / Robin / tracking",
    "Learn Skill / Robin / tracking",
    "Reassign / Galahad / warrior",
    "Perform / Galahad / warrior / healing",
    "Reassign / Galahad / healer",
    "Perform / Galahad / healer / healing",
    "End"
]);