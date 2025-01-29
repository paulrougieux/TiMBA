# Changelog

## [v1.0.2] - 2025-01-29

### Added
- **Python 3.12 compatibility**:
  - TiMBA is upgraded to run with Python 3.12.6.
  - Successfully tested for Python 3.9, 3.10, 3.11. 
- **GitHub Actions**: 
  - Set up GitHub Actions for TiMBA to integrate automated functionality and quality checks.
  - Added compatibility checks with multiple Python versions (Python 3.9, 3.10, 3.11, 3.12) and operating systems
(Windows and Ubuntu).
- **SonarCloud Integration**: Implemented and optimized code coverage and scans to ensure higher code quality.  
  - Integrated SonarCloud into the GitHub Actions pipeline.  
  - Added a SonarCloud quality status badge to `README.md`.   
- **Badges**: Added project badges like release status, coverage, and Zenodo-DOI.

### Changed
- **Package Upgrades**: All packages are upgraded to a version compatible with Python 3.12.
- **Readme & Compatibility**: Updated compatible Python versions and supported operating systems.
- **Scenario input file**: Changed scenario file for more consistent results.
- **Zipped pkl-files**: pkl-files for TiMBA output are zipped now to save storage space.
- **pkl-files with time stamps**: pkl-files for TiMBA output are now saved with a time stamp to allow unambiguous
identification.

### Fixed
- **GitHub Actions Bugs**:  
  - Various adaptations to fix bugs in the GitHub Actions 
- **Fixes to ensure compatibility with Python 3.12**
  - Resolved an issue with `np.isclose` for compatibility between Python 3.12 and Pandas.  
  - Replaced `iteritems` with `items` for compatibility with Python 3.12.
- **Gitignore Improvements**: Extended `.gitignore` to include additional folders like `timba\data\input`.

### Removed
- **Unnecessary Folders**: Removed virtual environment (`venv`) from the repository.  
- **Unsupported Python Versions**: Removed outdated versions from the test matrix.
