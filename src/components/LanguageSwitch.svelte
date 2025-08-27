<script lang="ts">
    import { siteConfig } from "../config";
    
    // Get current language from URL or config
    let currentLang = siteConfig.lang;
    
    // Language options
    const languages = [
        { code: "zh_CN", name: "中文", flag: "🇨🇳" },
        { code: "en", name: "English", flag: "🇺🇸" }
    ];
    
    // Note: Removed getCurrentPath() function as we now always redirect to homepage
    
    // Switch language
    function switchLanguage(langCode: string) {
        if (typeof window !== 'undefined') {
            // Save user preference to localStorage
            try {
                localStorage.setItem('preferred-language', langCode);
            } catch (e) {
                // localStorage not available, continue anyway
            }
            
            // Always redirect to homepage to avoid 404 errors
            const newPath = langCode === 'en' ? '/en/' : '/';
            
            // Navigate to homepage of selected language
            window.location.href = newPath;
        }
    }
    
    // Detect current language from URL
    if (typeof window !== 'undefined') {
        const path = window.location.pathname;
        if (path.startsWith('/en/')) {
            currentLang = 'en';
        } else {
            currentLang = 'zh_CN';
        }
    }
    
    let isOpen = false;
    
    function toggleDropdown() {
        isOpen = !isOpen;
    }
    
    function closeDropdown() {
        isOpen = false;
    }
</script>

<div class="relative inline-block text-left language-switch">
    <button 
        type="button" 
        class="btn-regular rounded-lg h-10 w-10 active:scale-90 flex items-center justify-center"
        on:click={toggleDropdown}
        aria-label="Switch Language"
    >
        {#each languages as lang}
            {#if lang.code === currentLang}
                <span class="text-xl">{lang.flag}</span>
            {/if}
        {/each}
    </button>
    
    {#if isOpen}
        <div 
            class="absolute right-0 mt-2 w-48 rounded-lg shadow-lg bg-[var(--card-bg)] border border-[var(--line-divider)] z-50"
            role="menu"
        >
            <div class="py-1" role="none">
                {#each languages as lang}
                    <button
                        class="flex items-center w-full px-4 py-2 text-sm hover:bg-[var(--btn-regular-bg)] transition-colors duration-200 {lang.code === currentLang ? 'text-[var(--primary)] font-medium' : 'text-[var(--content-text-color)]'}"
                        role="menuitem"
                        data-lang={lang.code}
                        on:click={() => {
                            switchLanguage(lang.code);
                            closeDropdown();
                        }}
                    >
                        <span class="mr-3 text-lg">{lang.flag}</span>
                        <span>{lang.name}</span>
                        {#if lang.code === currentLang}
                            <span class="ml-auto text-[var(--primary)]">✓</span>
                        {/if}
                    </button>
                {/each}
            </div>
        </div>
    {/if}
</div>

<!-- Click outside to close -->
{#if isOpen}
    <div 
        class="fixed inset-0 z-40" 
        on:click={closeDropdown}
        role="button" 
        tabindex="-1"
        on:keydown={() => {}}
    ></div>
{/if}

<style>
    /* Custom styles if needed */
</style>
