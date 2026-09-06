# Replacement and migration parity

Use when replacing a framework, UI, host, implementation, or workflow. Preserve user-visible capabilities and data semantics within the requested scope, while freely changing internals. Pixel-identical presentation, new features, and preservation of known defects are not implied. Explicit user-approved removals or a shell-only experiment narrow the target; project age does not.

## Establish the baseline before removal

1. Inventory existing user workflows from the implementation, requirements, tests, and migration documents. Include actions and results, not just screen names or backend modules. Record important success/error paths, settings persistence, import/export, cancellation, and platform behavior where present.
2. Put each workflow in the requirement map defined by [verification.md](verification.md): original source, new entrypoint, evidence, and remaining action. Existing parity tables remain acceptance authorities unless the user changes scope or evidence establishes a requirement error.
3. Ensure the old implementation and acceptance baseline can be recovered. Use an existing commit if it contains the files; an untracked repository or unborn branch needs a bounded snapshot or equivalent recoverable copy. Verify the recovery location before deletion. Do not create a commit or backup of unrelated/private material merely for convenience.

## Implement and verify workflows

For each row, connect the new entrypoint through the real service/data path to the visible result, then verify relevant old scenarios against it. Preserve behavioral assertions when replacing framework-specific tests. Navigation labels, placeholder pages, service extraction, and passing backend tests are intermediate progress.

Use manageable batches and bounded ownership, but retain all unfinished rows in the active backlog. An agent discovering missing features supplies implementation work, not permission to omit them. Keep migration facts separate from architecture preferences; "clean new implementation" describes structure, not reduced functionality.

## Cut over and remove

Before deleting the old implementation, obtain independent final parity review against the baseline and verify all required workflows in the integrated replacement. Then remove the superseded implementation and build chain, and re-run affected entrypoint and regression checks after cleanup. Preserve evidence and recovery information.

If keeping both implementations in the live build blocks the migration, isolate the old implementation as a recoverable reference while replacing the active path. Its workflows still remain in scope. If a genuine environment limitation prevents parity verification, preserve recovery and report the blocked requirements; do not claim complete migration.

Update docs and CI to the new architecture while keeping their functional acceptance obligations traceable. Replacing an old test command is valid; silently deleting the workflow it checked is not. Read [verification.md](verification.md) before delivery for the final continue/complete/blocked decision.
