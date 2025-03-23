async function run() {
    try {
        // Get the draft input from the Drafts app
        const draftInput = draft.content;
        const [title, rating] = draftInput.split("\n");
        const owner = draft.processTemplate("[[owner]]") || "mat-0";
        const repo = draft.processTemplate("[[repo]]") || "TheChels.uk";
        const token = draft.processTemplate("[[token]]");
        const workflow = "add-film.yml";
        const base_url = "https://api.github.com";
        const post_url =
            "${base_url}/repos/${owner}/${repo}/actions/workflows/${workflow}/dispatches";
        // Make a POST request to trigger the workflow dispatch
        const http = HTTP.create();
        const response = http.request({
            method: "POST",
            url: post_url,
            headers: {
                Authorization: `Bearer ${token}`,
                Accept: "application/vnd.github.v3+json",
                "Content-Type": "application/json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            data: JSON.stringify({
                ref: "main",
                inputs: {
                    title: title,
                    rating: rating,
                },
            }),
        });

        draft.append(`\n\n---\n\n`);
        draft.append(response.responseText);
        script.complete();
    } catch (error) {
        console.log(`Error: ${error}`);
        draft.append(`\n\n---\n\n`);
        draft.append(error);
        script.complete();
    }
}

// Run the function
run();
