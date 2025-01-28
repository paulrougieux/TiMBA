# Changelog

## [1.0.2] - 2025-01-28

### Added
- **SonarCloud Integration**: Implemented and optimized code coverage and scans to ensure higher code quality.  
  - Integrated SonarCloud into the GitHub Actions pipeline.  
  - Added a SonarCloud quality status badge to `README.md`.  
- **GitHub Actions Updates**:  
  - Added support for Python 3.12 and compatibility checks with multiple operating systems.  
  - Implemented code coverage with Codecov and SonarCloud.  
- **Badges**: Added project badges like release status and coverage.  
<!-- - **Documentation Enhancements**: Expanded and improved the documentation structure.  
  - Added new sections on software validation and usage.  
  - Included tables and additional data.  
- **New Directory**: Added a `documentation` folder for better organization. -->

### Changed
- **Path Updates**: Updated paths for `02_additional_information` to improve clarity.  
- **Package Upgrades**: Upgraded Pandas to version 2.2.3 for Python 3.12 compatibility.  
- **GitHub Actions**: Optimized triggers and target branches.  
- **Readme & Compatibility**: Updated compatible Python versions and supported operating systems.

### Fixed
- **GitHub Actions Bugs**:  
  - Fixed issues in pipelines (e.g., branch resets, unnecessary triggers).  
  - Resolved an issue with `np.isclose` for compatibility between Python and Pandas.  
  - Replaced `iteritems` with `items` for compatibility with Python 3.12.  
- **SonarQube Reports**: Fixed errors in code coverage report analysis.  
- **Gitignore Improvements**: Extended `.gitignore` to include additional folders like `timba\data\input`.  
<!-- - **Documentation Bugs**: Corrected typos and formatting issues in documentation. -->

### Removed
- **Unnecessary Folders**: Removed virtual environment (`venv`) from the repository.  
- **Unsupported Python Versions**: Removed outdated versions from the test matrix.

<!-- ### Documentation
- Significant updates to documentation:  
  - Improved chapters on introduction, overview, model specifications, and results.  
  - Converted Markdown documentation into PDF and DOCX formats.  
  - Enhanced software descriptions and added tables. -->

### Other
- **Minor Changes**:  
  - Small updates to `actions.yml` for workflow optimization.  
  - Reorganized scenario files for more consistent results.

<!-- - Merge pull request #62 from TI-Forest-Sector-Modelling/61-fix-sonarqube-coverage-report-analysis (8577c85)
- Reset action trigger to main (46e5bda)
- Test replace package pytest by coverage (4e87d6b)
- Test commit to verify SonarCloud functionality (448d2f1)
- Merge pull request #56 from TI-Forest-Sector-Modelling/30-add-timbadatainput-folder-to-gitignore (957c9db)
- fixed #30 in gitignore (4885873)
- fixed #17 and #27 (8b5c0dc)
- fixed #17 (a846704)
- fixed #60 (30ea9c2)
- Merge pull request #55 from TI-Forest-Sector-Modelling/main_issues_th (3f80f12)
- Merge pull request #54 from TI-Forest-Sector-Modelling/52-update-compatible-python-versions-and-os (3780450)
- Update readme with new Python versions and OS (1a3395e)
- Update documentation with new Python versions and OS (7482636)
- Merge pull request #53 from TI-Forest-Sector-Modelling/46-delete-venv-from-github-repo (3d38ed1)
- Delete unintentional venv folder (9b24b6d)
- Merge pull request #49 from TI-Forest-Sector-Modelling/47-add-sonarcloud-badge (ed650e4)
- Add sonarcloud badge in readme (5c123ac)
- Merge pull request #48 from TI-Forest-Sector-Modelling/31-change-folder-name-02_additional_informations-to-02_additional_information (2fc1adb)
- Adapt readme for new folder name (68e769f)
- Adapt path for new folder name (9b9a7c9)
- Add additional information to new folder (ad0d2a0)
- Merge pull request #45 from TI-Forest-Sector-Modelling/25-change-documentation-and-readme-for-the-use-of-python-312 (59034a2)
- Update Python version compatibility in readme (4762274)
- Merge pull request #43 from TI-Forest-Sector-Modelling/41-test-timba-with-python-38-312 (19e286a)
- Remove optional python versions (9d6f6a3)
- Add additional python versions (6ebae0d)
- Add additional python version to test (9323427)
- Merge pull request #42 from TI-Forest-Sector-Modelling/40-extend-github-actions-for-code-coverage-with-sonarqube (3a02ec2)
- Merge branch 'main_issues_th' into 40-extend-github-actions-for-code-coverage-with-sonarqube (9cf04ee)
- Reset branches to main in actions (fe2b551)
- Delete sonar from build (3d0e7ae)
- Change sonar action to version v1 (6f7684f)
- Change trigger for test (3c9f565)
- Add sonar into actions (3d928f3)
- Upload coverage report to SonarCloud (147a610)
- Add sonar scan with Python 3.9 (dcdf1be)
- Add sonar scan (857d60b)
- Add back Codecov (e6dbc65)
- Changes in SonarCloud scan (c9e7266)
- Test new pipeline (72a4c3a)
- Replace Codecov by SonarCloud (c134e12)
- Merge pull request #39 from TI-Forest-Sector-Modelling/24-extend-github-actions-for-python-312 (fcc5692)
- Merge branch 'main_issues_th' into 24-extend-github-actions-for-python-312 (4c09b20)
- Add comment on compatibility issue with Python and pandas (a19651b)
- Rest target branch to main (e60fe42)
- Test with Python version to 3.12.6 (6423208)
- Reset pandas to 1.5.3 (1af4a45)
- Merge pull request #38 from TI-Forest-Sector-Modelling/26-extend-github-actions-for-different-os (2242e69)
- Replace np.isclose() to ensure compatibility between Python 3.12 and pandas 2.2.3 (a25eb0f)
- Replace iteritems with items for compatibility issues between Python 3.12 and pandas 2.2.3 (c23f6db)
- Update pandas package for compatibility with Python 3.12 (e45580e)
- Align requirements with toml (730fea5)
- Remove macOS from actions.yml (2063ec4)
- Revert changes in unittest (96c5e75)
- Increase rel_tolerance for unittests (c19ca20)
- Test other OS in GitHub actions (4a3e004)
- Merge pull request #36 from TI-Forest-Sector-Modelling/18-add-badges-for-project-in-readme (5b8083d)
- Add release badge (1ecd87b)
- Add test for 3.12 in actions.yml (c805027)
- Merge pull request #35 from TI-Forest-Sector-Modelling/19-extend-github-actions-for-code-coverage-with-codecov (4369360)
- Reset branch name (cbaefd9)
- Merge pull request #34 from TI-Forest-Sector-Modelling/18-add-badges-for-project-in-readme (3d323b4)
- Bug fix in badges (6918f89)
- Add project badges (f362a20)
- bug fix in actions.yml (92d0802)
- Add coverage via Codecov in actions.yml (570eab9)
- Add code coverage report to actions.yml (d8824c3)
- Merge pull request #33 from TI-Forest-Sector-Modelling/8-complete-passage-about-software (b3202ba)
- Merge pull request #32 from TI-Forest-Sector-Modelling/28-documentation-overall-corrections (d3c7fd7)
- Add software description (4b47a3d)
- fixed #30 (1595dcb)
- Merge pull request #23 from TI-Forest-Sector-Modelling/main_issues_cm (96a5e9a)
- restoring original scenario_input (bc6430c)
- transfer markdown docu to pdf and docx (a95db63)
- Changes in tables and table descriptions (c9d5471)
- Changes in chapter Trade (b84ded9)
- Changes in chapter Manufacturing (51a5821)
- Changes in chapter Supply (6d7a253)
- Changes in chapter Demand (bd4cec2)
- Changes in chapter Model formulation and specifications (3b66132)
- Changes in chapter Summary (7dc8f9b)
- Changes in chapter Introduction (e8a885e)
- Changes in chapter Preface (78073c8)
- Merge pull request #22 from TI-Forest-Sector-Modelling/main_documentation_jt (f878771)
- Merge pull request #21 from TI-Forest-Sector-Modelling/main_GitHub_actions (a46a9c9)
- Merge pull request #16 from TI-Forest-Sector-Modelling/tomkeH-patch-1 (b2cc1d9)
- Update actions.yml (d79402b)
- Update actions.yml (08fca21)
- Update actions.yml (bdb3c7f)
- Update actions.yml (bc2f32e)
- Update actions.yml (a4181b0)
- Update actions.yml (c88ff1f)
- Update actions.yml (b18baf2)
- Update actions.yml (be296e9)
- Update actions.yml (bb277f9)
- Update actions.yml (48634e8)
- Create actions.yml (8a5fec6)
- Minor changes to DOCUMENTATION.md (d3c6f63)
- Fixed #10 add passage about validation (2647412)
- Fixed #6 Add tables to DOCUMENTATION.md (da3c760)
- Doumentation: add forest part, change tippos and add .bib and bibliografie to the documentation (baff3be)
- documentation text further development (00c46a6)
- fixed #4 (0e2e4ff)
- TiMBA works with Python version 3.12.6 (a09c3b9)
- fixed #2 Adjust elasticity of supply (797901c)
- add documentation folder (40c579a)
- Merge pull request #1 from TI-Forest-Sector-Modelling/main_joss_paper (c8b7413)
- add paper.md and paper.bib (9fd6a11)
- rename citation file (77f3d06)
- small fixes (2c27907)
- initial commit (0a050f3) -->