const currentVersion = await getLatestDocumentVersion(docId);
await waitForDocumentUpdate(docId);
const latestVersion = await getLatestDocumentVersion(docId);

if (latestVersion > currentVersion) {
    console.log("You have a new document update!");
}
