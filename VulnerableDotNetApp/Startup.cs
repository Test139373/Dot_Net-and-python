public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddControllers();
        
        // VULNERABLE: Disables anti-CSRF tokens
        services.AddMvc(options => options.Filters.Add(new IgnoreAntiforgeryTokenAttribute()));
    }

    public void Configure(IApplicationBuilder app)
    {
        // VULNERABLE: Disables security headers
        app.Use(async (ctx, next) => {
            ctx.Response.Headers.Remove("X-Content-Type-Options");
            await next();
        });
        
        app.UseRouting();
        app.UseEndpoints(endpoints => endpoints.MapControllers());
    }
}