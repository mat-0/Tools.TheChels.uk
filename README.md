
# Site

Hopefully helpful tools and a bit of a playground for experiments. The site uses Jekyll, a static site generator, on Ruby. DNS and SSL by Cloudflare. It also uses GitHub actions, GitHub issues, and Python for extensive automation.

## Configuration

There are several optional settings for you to configure. Use the `_config.yml` file in the repo.

## Running Jekyll Locally

To preview the site locally:

1. Install [Ruby](https://www.ruby-lang.org/en/documentation/installation/) and [Bundler](https://bundler.io/).
2. Install dependencies:

    ```sh
    bundle install
    ```

3. Start the Jekyll server:

    ```sh
    bundle exec jekyll serve --watch
    ```

4. Visit [http://localhost:4000](http://localhost:4000) in your browser.
