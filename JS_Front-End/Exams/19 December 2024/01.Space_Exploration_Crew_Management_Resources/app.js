function solve(inputArr) {
    const astronautsCount = Number(inputArr.shift());
    const crew = {};

    for (let i = 0; i < astronautsCount; i++) {
        const [astronautName, spacecraftSection, skillsInput] = inputArr.shift().split(' ');
        const skills = skillsInput.split(',');
        crew[astronautName] = {spacecraftSection, skills};
    }

    let commandLine = inputArr.shift();
    while(commandLine !== 'End') {
        const [command, astronautName, ...args] = commandLine.split(' / ');

        switch(command) {
            case 'Perform':
                const [spacecraftSection, skill] = args;

                if (crew[astronautName].spacecraftSection === spacecraftSection && crew[astronautName].skills.includes(skill)) {
                    console.log(`${astronautName} has successfully performed the skill: ${skill}!`);
                } else {
                    console.log(`${astronautName} cannot perform the skill: ${skill}.`);
                }
                break;
            case 'Transfer':
                const newSpacecraftSection = args[0];
                crew[astronautName].spacecraftSection =newSpacecraftSection;
                console.log(`${astronautName} has been transferred to: ${newSpacecraftSection}`);
                break;
            case 'Learn Skill':
                const newSkill = args[0];
                if(crew[astronautName].skills.includes(newSkill)) {
                    console.log(`${astronautName} already knows the skill: ${newSkill}.`);
                } else {
                    crew[astronautName].skills.push(newSkill);
                    console.log(`${astronautName} has learned a new skill: ${newSkill}.`);
                }
                break;
        }
        commandLine = inputArr.shift();
    }

    for (const astronaut in crew) {
        let result = `Astronaut: ${astronaut}, `;
        result += `Section: ${crew[astronaut].spacecraftSection}, `;
        result += `Skills: ${crew[astronaut].skills.sort((a, b) => a.localeCompare(b)).join(', ')}`
        
        console.log(result);
    }
}

solve([
  "2",
  "Alice command_module piloting,communications",
  "Bob engineering_bay repair,maintenance",
  "Perform / Alice / command_module / piloting",
  "Perform / Bob / command_module / repair",
  "Learn Skill / Alice / navigation",
  "Perform / Alice / command_module / navigation",
  "Transfer / Bob / command_module",
  "Perform / Bob / command_module / maintenance",
  "End"
]);
solve([
  "3",
  "Tom engineering_bay construction,maintenance",
  "Sara research_lab analysis,sampling",
  "Chris command_module piloting,communications",
  "Perform / Tom / engineering_bay / construction",
  "Learn Skill / Sara / robotics",
  "Perform / Sara / research_lab / robotics",
  "Transfer / Chris / research_lab",
  "Perform / Chris / research_lab / piloting",
  "Learn Skill / Tom / diagnostics",
  "Perform / Tom / engineering_bay / diagnostics",
  "End"
]);